# Supabase Setup Guide for Notes System

## Step 1: Create Supabase Account
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project" 
3. Sign up with GitHub (recommended since your site is on GitHub)
4. Create a new organization and project

## Step 2: Create Database Table
1. In your Supabase dashboard, go to **SQL Editor**
2. Run this SQL to create the notes table:

```sql
CREATE TABLE notes (
  id BIGSERIAL PRIMARY KEY,
  text TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security (RLS)
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations (for shared notes)
CREATE POLICY "Allow all operations" ON notes
  FOR ALL USING (true);
```

## Step 3: Get Your API Keys
1. Go to **Settings** → **API** in your Supabase dashboard
2. Copy your **Project URL** and **anon public** key
3. Replace the placeholders in `axar/axar-map.html`:

```javascript
const SUPABASE_URL = 'https://your-project-id.supabase.co';
const SUPABASE_ANON_KEY = 'your-anon-key-here';
```

## Step 4: Test the Setup
1. Open `axar/axar-map.html` in your browser
2. Click the **Notes** button
3. Try adding a note - it should work!

## Step 5: Deploy to GitHub
1. Commit and push your changes to GitHub
2. Your notes will now be persistent and shared across all users!

## Features You'll Get:
- ✅ **Persistent notes** - stored in cloud database
- ✅ **Shared across all users** - everyone sees the same notes
- ✅ **Works from anywhere** - no local server needed
- ✅ **Real-time updates** - instant sync
- ✅ **Free tier** - up to 500MB database, 50,000 monthly active users

## Troubleshooting:
- If notes don't load, check the browser console for errors
- Make sure your Supabase URL and key are correct
- Verify the database table was created successfully
- Check that RLS policies are set up correctly

## Security Note:
The current setup allows anyone to read/write notes. For production use, you might want to add user authentication or more restrictive policies. 