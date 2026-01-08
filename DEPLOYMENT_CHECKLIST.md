# 📦 Vercel Deployment - Quick Reference

## ✅ What You Need

### 1. **Environment Variables** (Set in Vercel Dashboard)

```bash
SECRET_KEY=<generate-with-openssl-rand-hex-32>
GROQ_API_KEY=gsk_<your-groq-api-key>
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai_course_db
```

### 2. **MongoDB Atlas Database** (FREE)

- Create at [cloud.mongodb.com](https://cloud.mongodb.com/)
- FREE M0 tier (512 MB storage)
- See [MONGODB_ATLAS_SETUP.md](MONGODB_ATLAS_SETUP.md) for detailed guide

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
   - `MONGODB_URI` = (from [cloud.mongodb.com](https://cloud.mongodb.com/))

2. **Create MongoDB Atlas** (see [MONGODB_ATLAS_SETUP.md](MONGODB_ATLAS_SETUP.md)):
   - Sign up at cloud.mongodb.com
   - Create FREE M0 cluster
   - Get connection string
   - Add to Vercel as `MONGODB_URI`

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

## 🍃 Get MongoDB Atlas (FREE)

**Quick Setup** (10 minutes):

1. Go to [cloud.mongodb.com](https://cloud.mongodb.com/)
2. Sign up (free, no credit card)
3. Create **M0 FREE** cluster
4. Create database user (save password!)
5. Whitelist IP: `0.0.0.0/0` (for Vercel)
6. Get connection string
7. Replace `<password>` and add database name

**Detailed Guide**: See [MONGODB_ATLAS_SETUP.md](MONGODB_ATLAS_SETUP.md)

**Connection String Format:**
```
mongodb+srv://username:password@cluster.mongodb.net/ai_course_db?retryWrites=true&w=majority
```

---

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| "Secret key required" | Set `SECRET_KEY` in Vercel env vars |
| "AI not responding" | Set `GROQ_API_KEY` in Vercel env vars |
| "Database error" | Set `MONGODB_URI` in Vercel env vars |
| "Connection timeout" | Whitelist `0.0.0.0/0` in MongoDB Atlas |
| "Authentication failed" | Check password in MongoDB connection string |
| "Module not found" | Check `requirements.txt` has all packages |

---

## 📝 Checklist

Before deploying:
- [ ] Code pushed to GitHub
- [ ] Vercel project created
- [ ] `SECRET_KEY` environment variable set
- [ ] `GROQ_API_KEY` environment variable set
- [ ] MongoDB Atlas account created
- [ ] MongoDB cluster created (FREE M0)
- [ ] Database user created
- [ ] IP `0.0.0.0/0` whitelisted
- [ ] `MONGODB_URI` environment variable set
- [ ] Redeployed after adding env vars

---

## 🎯 Your Current Setup

**Repository**: `Rudhr07/ai-course-management`
**Files Ready**: All configured for Vercel
**Database**: MongoDB Atlas (free tier, 512 MB)
**AI Backend**: Groq API (free tier)

**Estimated Time**: 15-20 minutes for first deployment

---

## 🆓 100% Free Stack

- ✅ **Vercel Hosting**: Free forever
- ✅ **MongoDB Atlas**: 512 MB free tier
- ✅ **Groq API**: 14,400 requests/day free
- ✅ **Total Cost**: $0/month 💰
