FROM node:20-bookworm-slim
RUN apt-get update && apt-get install -y python3 python3-pip unzip && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY amrit_mental_fullstack.zip .
RUN unzip -o amrit_mental_fullstack.zip

# 🔒 SECURITY PATCH: HIDE PUBLIC BOTS + ADMIN PASSWORD PANEL (amrit@admin99)
RUN python3 -c '\
import os, re;\
admin_middleware = """\n\
const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || "amrit@admin99";\n\
app.use((req, res, next) => {\n\
    const isInstanceRoute = req.path.includes("/api/instances") || req.path.includes("/api/bots");\n\
    if (isInstanceRoute) {\n\
        const clientPass = req.headers["x-admin-pass"] || req.query.adminPass;\n\
        if (req.method === "POST") return next();\n\
        if (clientPass !== ADMIN_PASSWORD) {\n\
            if (req.method === "GET") return res.json([]);\n\
            return res.status(403).json({ error: "Unauthorized! Only Admin can manage bots." });\n\
        }\n\
    }\n\
    next();\n\
});\n\
""";\
if os.path.exists("server.ts"):\
    with open("server.ts", "r", encoding="utf-8", errors="ignore") as f:\
        s = f.read();\
    if "const ADMIN_PASSWORD" not in s:\
        pattern = r"(app\s*=\s*express\(\);?)";\
        if re.search(pattern, s):\
            s = re.sub(pattern, r"\1" + admin_middleware, s, count=1);\
            with open("server.ts", "w", encoding="utf-8") as f:\
                f.write(s);\
            print("server.ts secured with Admin Password!");\
admin_btn_script = """\n\
<script>\n\
(function(){\n\
  var p = localStorage.getItem("amrit_admin_pass");\n\
  var b = document.createElement("button");\n\
  b.id = "amrit-admin-btn";\n\
  b.innerHTML = p ? "🛡️ Admin Active" : "🔒 Admin Login";\n\
  b.style.cssText = "position:fixed;bottom:18px;right:18px;z-index:999999;padding:10px 16px;background:" + (p ? "#059669" : "#2563eb") + ";color:#ffffff;border-radius:30px;font-size:13px;font-weight:bold;border:2px solid #ffffff;cursor:pointer;box-shadow:0 6px 18px rgba(0,0,0,0.6);font-family:sans-serif;";\n\
  b.onclick = function(){\n\
    var cur = localStorage.getItem("amrit_admin_pass");\n\
    if(cur){\n\
      if(confirm("Logout from Admin mode?")){\n\
        localStorage.removeItem("amrit_admin_pass");\n\
        location.href = location.pathname;\n\
      }\n\
    } else {\n\
      var pass = prompt("Enter Master Admin Password:");\n\
      if(pass === "amrit@admin99"){\n\
        localStorage.setItem("amrit_admin_pass", pass);\n\
        alert("✅ Welcome AMRIT! Admin panel activated.");\n\
        location.search = "?adminPass=" + pass;\n\
      } else if(pass){\n\
        alert("❌ Galat Password! Sirf Admin access kar sakta hai.");\n\
      }\n\
    }\n\
  };\n\
  window.addEventListener("DOMContentLoaded", function(){ document.body.appendChild(b); });\n\
  if(document.body) document.body.appendChild(b);\n\
  if(p && !location.search.includes("adminPass=")){\n\
    location.search = "?adminPass=" + p;\n\
  }\n\
})();\n\
</script>\n\
""";\
for h in ["index.html", "public/index.html"]:\
    if os.path.exists(h):\
        with open(h, "r", encoding="utf-8", errors="ignore") as f:\
            hc = f.read();\
        if "amrit-admin-btn" not in hc:\
            hc = hc.replace("</body>", admin_btn_script + "\n</body>");\
            with open(h, "w", encoding="utf-8") as f:\
                f.write(hc);\
'

RUN pip3 install --no-cache-dir --break-system-packages python-telegram-bot==21.6 httpx aiohttp
RUN npm install --legacy-peer-deps
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
