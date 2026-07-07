# AI Lab Command Center — Architecture Playbook

Operator archive for the ai-lab-command-center monetization stack.
This playbook is the public backend reference linked from the product README.

## Endpoints

| Purpose | Route | Notes |
|---------|-------|-------|
| Fulfillment | `POST /api/revenue-os/products/{slug}/fulfill` | Writes event, triggers post-purchase email, record download |
| Download | `GET /api/revenue-os/products/{slug}/download/{event_file}` | Serves latest tarball for purchased slug |
| Health | `GET /health` | service health |
| Summary | `GET /api/revenue-os/summary` | revenue rollup |

## Buyer docs location
`/home/scott/ai-lab/productization/generated-buyer-docs/<slug>`

## Deliverable archive
`/home/scott/ai-lab/reports/deliverables/<slug>-YYYYMMDD-HHMMSS.tar.gz`

## Links

### Product landing pages
- [Hardonian README](https://github.com/Hardonian/Hardonian/blob/main/README.md)
- [Local AI Lab Audit](https://github.com/Hardonian/Hardonian/blob/main/products/local-ai-lab-audit.md)
- [AI Command Center Setup](https://github.com/Hardonian/Hardonian/blob/main/products/ai-command-center-setup.md)
- [ComfyUI Workflow Packs](https://github.com/Hardonian/Hardonian/blob/main/products/comfyui-workflow-packs.md)

### Operator portal
- [AI Lab Command Center dashboard](https://github.com/Hardonian/ai-lab-command-center)

## Playbook usage rules
- keep payer-facing marketing claims factual and sourced from `revenue-os/products/<slug>/product.json`
- buyer docs path is the canonical deliverable location; never invent a new copy without regenerating from current tar
- fulfill mutations only run through `/api/revenue-os/products/{slug}/fulfill` or verified stripe handler

## Changelog
- 2026-07-06: Initial architecture-playbook content added for public product-page linkage.
