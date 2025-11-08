import json
import frappe

def import_products_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for product in data:
        try:
            create_item_template_and_variants(product)
        except Exception as e:
            frappe.log_error(f"Error importing {product.get('title')}: {str(e)}")

def create_item_template_and_variants(product):
    if frappe.db.exists("Item", product['handle']):
        return

    template = frappe.get_doc({
        "doctype": "Item",
        "item_code": product['handle'],
        "item_name": product['title'],
        "item_group": product.get('product_type') or "Uncategorized",
        "stock_uom": "Nos",
        "has_variants": 1,
        "description": product.get('body_html') or "",
        "shopify_product_id": product['id']
    })
    template.insert(ignore_permissions=True)

    for variant in product.get("variants", []):
        sku = variant.get("sku") or f"VAR-{variant['id']}"
        if frappe.db.exists("Item", sku):
            continue

        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": sku,
            "item_name": variant.get("title") or sku,
            "variant_of": template.name,
            "shopify_variant_id": variant['id']
        })
        item.insert(ignore_permissions=True)

    frappe.db.commit()
