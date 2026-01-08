# 🚀 Vercel Deployment Guide

## ⚠️ Important: Database Configuration

**SQLite won't work on Vercel** (serverless environments have no persistent storage).

You have **two options**:

### Option 1: PostgreSQL (Recommended) ✅

Use **Vercel Postgres** (free tier available):

1. Go to your Vercel project → **Storage** → **Create Database** → **Postgres**
2. Vercel will automatically add these environment variables:
   - `POSTGRES_URL`
   - `POSTGRES_PRISMA_URL`
   - `POSTGRES_URL_NON_POOLING`

3. Update `app.py` database URI:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///cms.db')
   ```

4. Add `psycopg2-binary` to requirements.txt

### Option 2: MySQL/MongoDB

Use external database services:
- **PlanetScale** (MySQL) - Free tier
- **MongoDB Atlas** - Free tier
- **Railway** - Free tier with PostgreSQL

---

## 📋 Required Environment Variables (Vercel Dashboard)

Set these in **Vercel Dashboard** → **Settings** → **Environment Variables**:

| Variable | Value | Required? |
|----------|-------|-----------|
| `SECRET_KEY` | Any random string (e.g., use `python -c "import secrets; print(secrets.token_hex(32))"`) | ✅ YES |
| `GROQ_API_KEY` | Get from [console.groq.com](https://console.groq.com/) | ✅ YES (for AI) |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | ⚪ Optional |
| `DATABASE_URL` | PostgreSQL connection string | ✅ YES (if using Postgres) |

---

## 🔧 Deployment Steps

### 1. **Update Database Configuration**

Replace SQLite with PostgreSQL in `app.py`:

```python
# Old (SQLite - won't work on Vercel)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'

# New (PostgreSQL - works on Vercel)
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///cms.db')
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
```

### 2. **Update requirements.txt**

Add PostgreSQL driver:
```
Flask==2.3.3
Flask-Login==0.6.2
Flask-SQLAlchemy==3.0.3
requests==2.31.0
Werkzeug==2.3.7
psycopg2-binary==2.9.9
```

### 3. **Push to GitHub**

```bash
git add .
git commit -m "Configure for Vercel deployment"
git push origin main
```

### 4. **Deploy on Vercel**

#### Option A: Vercel CLI
```bash
npm i -g vercel
vercel login
vercel --prod
```

#### Option B: Vercel Dashboard
1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Vercel auto-detects `vercel.json` configuration
4. Click **Deploy**

### 5. **Add Environment Variables**

In Vercel Dashboard:
1. Go to **Settings** → **Environment Variables**
2. Add:
   - `SECRET_KEY` = (generate with `openssl rand -hex 32`)
   - `GROQ_API_KEY` = (from console.groq.com)
3. Click **Save**
4. **Redeploy** to apply changes

### 6. **Create Database**

1. Go to **Storage** tab in Vercel
2. Click **Create Database** → **Postgres**
3. Vercel auto-adds `DATABASE_URL`
4. **Redeploy** again

---

## ✅ Checklist Before Deployment

- [ ] Updated `app.py` to use PostgreSQL
- [ ] Added `psycopg2-binary` to requirements.txt
- [ ] Pushed code to GitHub
- [ ] Created Vercel project
- [ ] Set `SECRET_KEY` environment variable
- [ ] Set `GROQ_API_KEY` environment variable
- [ ] Created Vercel Postgres database
- [ ] Redeployed after adding environment variables

---

## 🧪 Testing Deployment

After deployment:
1. Visit your Vercel URL (e.g., `your-app.vercel.app`)
2. Sign up for a new account
3. Add courses to a semester
4. Test AI chatbot
5. Test semester summarization

---

## 🐛 Common Issues

### Issue: "Module not found" error
**Solution**: Make sure all dependencies are in `requirements.txt`

### Issue: "Database connection failed"
**Solution**: Check `DATABASE_URL` is set in environment variables

### Issue: "AI not responding"
**Solution**: Verify `GROQ_API_KEY` is correctly set (starts with `gsk_`)

### Issue: "Session errors"
**Solution**: Ensure `SECRET_KEY` is set and is a strong random string

---

## 📊 Free Tier Limits

### Vercel
- ✅ Unlimited deployments
- ✅ 100 GB bandwidth/month
- ✅ Serverless function execution

### Vercel Postgres
- ✅ 256 MB storage
- ✅ 60 hours compute/month
- ✅ 256 MB RAM

### Groq API
- ✅ 14,400 requests/day
- ✅ Generous token limits
- ✅ Fast inference

---

## 🎯 Quick Deploy (TL;DR)

```bash
# 1. Update app.py for PostgreSQL
# 2. Update requirements.txt
pip freeze > requirements.txt

# 3. Push to GitHub
git add .
git commit -m "Ready for Vercel"
git push origin main

# 4. Deploy
vercel --prod

# 5. Add environment variables in Vercel Dashboard
# 6. Create Postgres database in Vercel
# 7. Redeploy
```

**Done!** Your app is live at `https://your-project.vercel.app` 🎉
