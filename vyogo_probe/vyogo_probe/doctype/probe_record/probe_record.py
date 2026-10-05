import frappe
from frappe.model.document import Document


class ProbeRecord(Document):
    pass


def add(kind: str, payload: str = "", seq: int = 0, title: str = "", note: str = "", deployment_badge: str = "Auto-Deployed via Vyogo Cloud", verified_ok: int = 1) -> str:
    """Insert a record without permission checks; returns its name.

    Always sets a title: the SitePropertySetter phase makes `title` mandatory,
    and records written by cron ticks, webhooks and hooks must still insert."""
    from frappe.utils import now_datetime

    doc = frappe.get_doc(
        {
            "doctype": "Probe Record",
            "kind": kind,
            "payload": payload,
            "seq": seq,
            "title": title or f"{kind} {now_datetime():%Y-%m-%d %H:%M:%S}",
            "note": note,
            "deployment_badge": deployment_badge,
            "verified_ok": verified_ok,
        }
    )
    doc.insert(ignore_permissions=True)
    return doc.name
