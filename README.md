# Saarthak's Portfolio

A minimal, clean portfolio website inspired by Himanshu's design.

## 🚀 Quick Start

**Option 1: Double-click `index.html`**  
Simply open `index.html` in any browser - no setup required!

**Option 2: Local Server**
```bash
# Using Python
python -m http.server 8000

# Then visit: http://localhost:8000
```

## ✨ Features

- **Minimal Design**: Clean aesthetic with smooth animations
- **Unique Icons**: Generated SVG images instead of common emojis
- **Bullet Point Descriptions**: Technical expertise clearly highlighted
- **Responsive**: Works on all devices
- **Pure HTML/CSS/JS**: No build process needed

## 📂 Sections

### Navigation
- **Home**: Main portfolio page
- **Posts**: Technical deep dives and ML blog posts

### Home Section
- **What I Do**: Contract-based ML Engineer role (Jun 2025 - Oct 2025)
- **Education**: BTech ECE from IIIT Delhi (Nov 2022 - Present)
- **Projects**: Featuring 2 key projects (Docbook, Bayesian Course Rec)
- **What Excites Me**: Focus on ML research & generative engine optimization
- **Connect**: GitHub and X/Twitter links

### Posts Section
- **Bayesian Personalized Ranking**: Deep dive into BPR for implicit feedback systems
- **Graph Neural Networks**: Comprehensive GNN exploration (first draft)

## 📝 To-Do

### Update Content:
1. **Email**: Replace `your.email@example.com` in `index.html` (if you want to add email functionality)
2. ✅ **ML Engineer Details**: Added! Chemical reaction prediction GNN work
3. ✅ **Profile Picture**: Updated with profile.png

### How to Add Your X Profile Picture:

**Method 1: Direct URL from X**
1. Go to [your X profile](https://x.com/curlysaarthak)
2. Right-click on your profile picture
3. Select "Open image in new tab"
4. Copy the URL (it will look like: `https://pbs.twimg.com/profile_images/...`)
5. Replace the `src` in line ~26 of `index.html` with this URL

**Method 2: Upload Image to Portfolio Folder**
1. Download your profile picture from X
2. Save it in the portfolio folder as `profile.jpg` or `profile.png`
3. Update the `src` in `index.html` to: `src="profile.jpg"`

### Optional Customizations:
- Change icon colors: Update the `backgroundColor` parameter in image URLs
- Update project details: Modify bullet points to reflect your work

## 🎨 Design Elements

**Profile Picture**: Horizontally aligned with name (Himanshu-style layout)  
**Project Icons**: Abstract shapes with custom colors  
**X Logo**: Clean inline SVG icon in footer (no blue button!)  
**Animations**: Smooth fade-in on scroll

## 📂 Structure

```
portfolio/
├── index.html      # Main HTML structure
├── style.css       # Styling
├── script.js       # Animations & interactions
└── README.md       # This file
```

## 🔗 Links in Portfolio

- GitHub: [@Saarthakkj](https://github.com/Saarthakkj)
- X/Twitter: [@curlysaarthak](https://x.com/curlysaarthak)

## 💡 Customization Tips

**Change Icon Colors:**  
In `index.html`, find the image URLs and change the `backgroundColor` parameter:
```html
backgroundColor=4f46e5  <!-- Indigo -->
backgroundColor=10b981  <!-- Green -->
backgroundColor=f59e0b  <!-- Orange -->
```

**Add More Projects:**  
Copy a project-item div and modify the content:
```html
<div class="project-item">
    <img src="https://api.dicebear.com/7.x/shapes/svg?seed=yourproject&backgroundColor=your-color" alt="Project" class="project-icon">
    <div class="project-content">
        <h3>Project Name</h3>
        <ul class="project-description">
            <li>Key feature 1</li>
            <li>Key feature 2</li>
        </ul>
        <div class="tech-tags">
            <span class="tech-tag">Tech 1</span>
        </div>
    </div>
</div>
```

---

Made with ❤️ and minimal code

