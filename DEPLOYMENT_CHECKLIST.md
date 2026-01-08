# 📦 Vercel Deployment - Quick Reference

## ✅ What You Need

### 1. **Environment Variables** (Set in Vercel Dashboard)

```bash
SECRET_KEY=<generate-with-openssl-rand-hex-32>
GROQ_API_KEY=gsk_<your-groq-api-key>
```

### 2. **Vercel Postgres Database**

- Create in Vercel Dashboard → **Storage** → **Postgres**
- `DATABASE_URL` is auto-added by Vercel

### 3. **Files Already Configured** ✅

- [x] `vercel.json` - Vercel configuration
- [x] `requirements.txt` - Python dependencies (includes psycopg2-binary)
- [x] `app.py` - Updated to support PostgreSQL
- [x] `.env.example` - Environment variable template
- [x] `.gitignore` - Excludes sensitive files

---

## 🚀 Deploy in 3 Steps

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

### Step 2: Import to Vercel
1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repo: `Rudhr07/ai-course-management`
3. Click **Deploy** (will fail without env vars - that's OK!)

### Step 3: Configure Environment
1. **Add Variables**: Settings → Environment Variables
   - `SECRET_KEY` = (run: `openssl rand -hex 32`)
   - `GROQ_API_KEY` = (from [console.groq.com](https://console.groq.com/))

2. **Add Database**: Storage → Create Database → Postgres

3. **Redeploy**: Deployments → Click ⋯ → Redeploy

**Done!** Visit your app at `https://your-project.vercel.app` 🎉

---

## 🔑 Get Groq API Key (FREE)

1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up with GitHub/Google
3. Click **API Keys** → **Create API Key**
4. Copy key (starts with `gsk_`)
5. Paste in Vercel environment variables

**Free Tier**: 14,400 requests/day, plenty for your app!

---

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| "Secret key required" | Set `SECRET_KEY` in Vercel env vars |
| "AI not responding" | Set `GROQ_API_KEY` in Vercel env vars |
| "Database error" | Create Vercel Postgres in Storage tab |
| "Module not found" | Check `requirements.txt` has all packages |

---

## 📝 Checklist

Before deploying:
- [ ] Code pushed to GitHub
- [ ] Vercel project created
- [ ] `SECRET_KEY` environment variable set
- [ ] `GROQ_API_KEY` environment variable set
- [ ] Vercel Postgres database created
- [ ] Redeployed after adding env vars

---

## 🎯 Your Current Setup

**Repository**: `Rudhr07/ai-course-management`
**Files Ready**: All configured for Vercel
**Database**: Will use Vercel Postgres (free tier)
**AI Backend**: Groq API (free tier)

**Estimated Time**: 5-10 minutes for first deployment
