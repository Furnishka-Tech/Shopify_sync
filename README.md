# 🛠️ Furnishka ERPNext ↔ Shopify Product Sync

This repo contains scripts and documentation for syncing products from Shopify to ERPNext and making ERPNext the source of truth.

## 📁 Structure

- `scripts/import_shopify_products.py`: Import Shopify products into ERPNext
- `scripts/attach_images.py`: Upload and link product images to ERPNext
- `README.md`: Full implementation playbook

---

## 🚀 Getting Started

1. Export products from Shopify via API or JSON dump
2. Update `import_shopify_products.py` with your JSON path
3. Run inside a Frappe bench environment
