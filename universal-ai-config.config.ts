import { defineConfig } from "universal-ai-config";

export default defineConfig({
  targets: ["claude", "cursor"],
  variables: {
    projectName: "speckle-fme",
  },
});
