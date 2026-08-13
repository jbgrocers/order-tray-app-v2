# Order Tray App (Frappe-hosted frontend)

This is a lightweight Frappe app whose only job is to serve the built
**Order Tray React UI** as a page on your existing Frappe Cloud site —
no separate hosting account needed.

Once installed on `jbgrocers.jh.frappe.cloud`, the Order Tray UI will be
live at:

```
https://jbgrocers.jh.frappe.cloud/order-tray
```

The React app itself is unchanged — it still talks to your existing
Frappe REST API and Socket.io real-time updates. This package just adds
one static webpage (`www/order-tray.html`) plus the compiled
JS/CSS bundle (`public/order-tray/`).

## What's Inside

```
order_tray_app/
├── order_tray_app/
│   ├── __init__.py
│   ├── hooks.py                     # App registration, no backend logic added
│   ├── modules.txt
│   ├── www/
│   │   └── order-tray.html          # The page served at /order-tray
│   └── public/
│       └── order-tray/
│           ├── index.js             # Compiled React app (264 KB)
│           └── index.css            # Compiled styles (17 KB)
├── setup.py
├── requirements.txt
├── MANIFEST.in
└── license.txt
```

## How to Deploy on Frappe Cloud

### Option A: Via Frappe Cloud Dashboard (Recommended, no CLI needed)

1. Push this folder to a new GitHub repo, e.g. `jbgrocers/order-tray-app`
2. Log into **Frappe Cloud** → select your `jbgrocers.jh.frappe.cloud` site's Bench
3. Go to **Apps** → **Install App from GitHub**
4. Paste the repo URL: `https://github.com/jbgrocers/order-tray-app`
5. Select branch `main`, click **Install**
6. Frappe Cloud will build and deploy automatically
7. Once deployed, visit: `https://jbgrocers.jh.frappe.cloud/order-tray`

### Option B: Via Bench CLI (if you manage the server directly)

```bash
cd frappe-bench
bench get-app https://github.com/jbgrocers/order-tray-app
bench --site jbgrocers.jh.frappe.cloud install-app order_tray_app
bench build --app order_tray_app
bench restart
```

## Updating the Frontend Later

Whenever the React app changes:
1. Rebuild it: `npm run build` (in the `order-tray-ui` repo)
2. Copy the new files from `dist/assets/*.js` → `order_tray_app/public/order-tray/index.js`
   and `dist/assets/*.css` → `order_tray_app/public/order-tray/index.css`
3. Commit and push to this repo
4. On Frappe Cloud, click **Deploy** (or re-run `bench update` / CLI steps above)

## Why This Approach

- **No new hosting account** — uses your existing Frappe Cloud subscription
- **No CORS issues** — frontend and backend share the same domain
- **No extra cost** — nothing beyond what you already pay for
- **Fits your existing deploy workflow** — same as your server script updates

## Notes

- This app adds **zero new database tables, doctypes, or server-side logic**.
  It is purely a static file server for the frontend.
- If you'd rather the app live at the root domain instead of `/order-tray`,
  rename `www/order-tray.html` to `www/index.html` (this will override the
  default Frappe login/desk landing page — only do this if you're sure
  that's what you want).
