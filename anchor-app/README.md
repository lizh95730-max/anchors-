# AnchorApp (iOS)

This is a native SwiftUI iOS app scaffold that loads requirements from a bundled JSON file generated from your documents.

## How to use your documents

1. Place the following files in `docs/` at the repo root:
   - `docs/Anchor_App_PRD.docx`
   - `docs/Anchor_App_Execution_Plan.docx`
2. Generate the requirements JSON:
   ```bash
   cd anchor-app
   pip install -r requirements.txt
   python3 scripts/extract_requirements.py
   ```
3. The script will produce `Resources/requirements.json`, which the app will display.

## Generate the Xcode project (on macOS)

This project uses [XcodeGen](https://github.com/yonaskolb/XcodeGen) to generate the Xcode project.

1. Install XcodeGen on macOS (e.g., `brew install xcodegen`).
2. Generate the project:
   ```bash
   cd anchor-app
   xcodegen generate
   open AnchorApp.xcodeproj
   ```
3. Select a simulator and Run.

## Tech
- Swift 5, SwiftUI
- iOS 16+

## Notes
- If `Resources/requirements.json` is missing, the app falls back to `Resources/requirements.sample.json`.
- Replace the sample data by adding your DOCX files and running the script above.