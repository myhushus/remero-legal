# Apply Remero Legal Content v1

If you unzip this package in `~/Downloads`, run:

```bash
cd ~/Downloads
unzip remero-legal-content-v1-delete-url.zip
cd ~/Downloads/remero-legal-upload
rsync -a ~/Downloads/remero-legal-content-v1-delete-url/ ./
git status
git add .
git commit -m "Publish Remero legal document v1"
git push origin main
```
