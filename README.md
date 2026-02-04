# Email Spam Detector

<img align="left" src=".github/assets/icon.png" width="25%"/>

ML-based **email spam classification** with a **FastAPI inference backend** and a **browser extension UI** for real-world use. It uses a trained ML model to analyze email content and serve predictions through a simple API that connects directly to the browser extension.  
For more information, see the [Getting Started](https://github.com/viraj-sh/email-spam-detector/wiki/Getting-Started) wiki page.

<a href="https://github.com/viraj-sh/email-spam-detector/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/viraj-sh/email-spam-detector/backend-build.yml?logo=githubactions&label=CI&logoColor=white&color=2563eb" alt="Github Actions">
</a>
<a href="https://github.com/viraj-sh/email-spam-detector/wiki">
    <img src="https://img.shields.io/badge/Wiki-%23000000.svg?logo=gitbook&label=Docs&logoColor=white&color=2563eb" alt="Github Wiki">
</a>
<a href="https://github.com/viraj-sh/email-spam-detector/releases/latest">
    <img src="https://img.shields.io/github/v/release/viraj-sh/email-spam-detector?label=Release&logoColor=white&color=2563eb" alt="Github Release">
</a>
<!-- <a href="https://hub.docker.com/r/virajsh/email-spam-detector">
    <img src="https://img.shields.io/docker/v/virajsh/email-spam-detector?logo=docker&label=Docker&logoColor=white&color=2563eb&sort=semver" alt="Docker Image">
</a> -->
<a href="https://github.com/viraj-sh/email-spam-detector/blob/main/requirements/base.txt">
    <img src="https://img.shields.io/badge/Python-3.13.5-blue.svg?logo=python&label=Python&logoColor=white&color=2563eb" alt="Docker Image">
</a>


<img src=".github/assets/line-blue.png" alt="line break" width="100%" height="3px">

## Quick Start

> A **FastAPI backend** and a **Chrome extension for Gmail** are required.

### 1. Run the Backend

#### Option A — Use a Prebuilt Release (Recommended)

Download and run the backend build for your operating system:

<a href="https://github.com/viraj-sh/email-spam-detector/releases">
    <img src="https://img.shields.io/badge/Windows-x64-2563eb?label=Windows&color=white" alt="Windows Release">
</a>
<a href="https://github.com/viraj-sh/email-spam-detector/releases">
    <img src="https://img.shields.io/badge/Linux-x86__64-2563eb?label=Linux&color=white" alt="Linux Release">
</a>
<a href="https://github.com/viraj-sh/email-spam-detector/releases">
    <img src="https://img.shields.io/badge/macOS-arm64-2563eb?label=macOS&color=white" alt="macOS Release">
</a>

#### Option B — Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/viraj-sh/email-spam-detector)

> For additional setup methods (source build, Docker, etc.), see **Wiki → [Getting Started](https://github.com/viraj-sh/email-spam-detector/wiki/Getting-Started)**.

---

### 2. Install the Browser Extension

1. Download the **extension `.zip` file** from the [**Releases**](https://github.com/viraj-sh/email-spam-detector/releases) section.
2. Extract the archive to a folder on your computer.
3. Open Chrome and go to:
   [`chrome://extensions/`](chrome://extensions/)
4. Enable **Developer mode** (top right).
5. Click **Load unpacked**.
6. Select the extracted extension folder.

---

### 3. Connect the Extension to Your Backend

1. Click the extension icon in Chrome.
2. Enter the URL where your backend is running
   Example: `http://localhost:8000`

##### Understanding the Extension Status Icons

| Icon      | Meaning                                                   |
| ---------- | --------------------------------------------------------- |
| <img align="left" src="browser-extension/public/icons/red/icon-red-48.png" width="50%"/> | Backend is not reachable                                  |
| <img align="left" src="browser-extension/public/icons/yellow/icon-yellow-48.png" width="50%"/> | Backend is connected, but you are not on a supported page |
| <img align="left" src="browser-extension/public/icons/green/icon-green-48.png" width="50%"/> | Backend is connected and the extension is active          |

> Currently, the extension only runs on [**`mail.google.com`**](https://mail.google.com/). Support for additional sites may be added in the future.

<img src=".github/assets/line-blue.png" alt="line break" width="100%" height="3px">

## Spam Detection Model

| Component         | Details                                                 |
| ----------------- | ------------------------------------------------------- |
| **Vectorization** | TF-IDF                                                  |
| **Classifier**    | Linear SVM                                              |
| **Library**       | scikit-learn                                            |
| **Dataset**       | CSV files in `./dataset/`                               |
| **Preprocessing** | Custom `clean_text()` function in `./app/core/utils.py` |
| **Tuning**        | Grid Search with Cross-Validation                       |
| **Saved Model**   | Stored with `joblib` in `./app/model/`                  |

<img src=".github/assets/line-blue.png" alt="line break" width="100%" height="3px">

## Project Status

In **Partial Development**
**Check out [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.**
