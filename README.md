# Acknowlegements
* Tribute to: [yonggekkk](https://github.com/yonggekkk)
* OG Repo: [Replit-Xray](https://github.com/yonggekkk/Replit-Xray/tree/main)
* [YouTube instructions](https://www.youtube.com/watch?v=p1G_yLCcIq0)
* Fragment base code: [config2Fragment](https://github.com/Surfboardv2ray/config2Fragment)

# How to Repl It
Here's the simplified steps to run an Argo Tunnel config based on Replit.

1. Create a replit account, tap `+ Create Repl` in the upper left corner of the homepage or the plus sign in the upper right corner
2. Search for the template: `Blank Repl`, enter the project name title, and tap Create Repl.
3. Download the compressed file `vmvltrssso.zip` and unzip it. Then drag all four decompressed files to the file bar on the left and confirm overwriting.
4. Tap `Run` and in the upper right corner under "web view", located and tap `New Tab`.
5. Separate the first part of the new tab URL (at the time of writing, it's in the format of `UUID.pike.replit.dev` -- make sure to exclude the "https://") and copy it.
6. Under "Tools" at left lower corner, locate and tap `Secrets`. Tap `New Secret`.
7. Name the "Key" as `ym` (lowercase) and put the address that you copied in step 5 as the "Value" of the secret.
8. `Stop` and `Run` again, this time you'll get html links under "Console".

# How to use
Since the argo tunnel address changes at every run, this code is an attempt to fetch the vless config every time that it changes.

9. Make sure your Repl is running.
10. Open `fetch-argo.py` and replace "YOUR_URL", "HOST_SNI" and "TARGET_IP".
11. `YOUR_URL`: This is link to your detailed configs link, the "new tab" in step 4.
12. `HOST_SNI`: This is the first part of the URL mentioned in step 5.
13. `TARGET_IP`: Clean CF IP or Domain.

# Notes
* So far, this code only returns the "vless://" config and base64 too. If needed, argo configs for vmess, trojan, ss and socks can be added as well.
* Replit code will run until the window is open, so while this saves the effort to get the argo config, this all is for educational purposes only and no abuse of services is intended.
