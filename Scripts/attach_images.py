import requests
from frappe.utils.file_manager import save_url
import frappe

def attach_shopify_image(item_code, image_url):
    save_url(image_url, item_code, "Item", item_code, is_private=0)
    item = frappe.get_doc("Item", item_code)
    item.item_image = image_url
    item.append("item_images", {"image": image_url})
    item.save()
