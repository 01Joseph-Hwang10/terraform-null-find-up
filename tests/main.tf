
module "workspace_root" {
  source = "../"

  targets = "version.txt"
}

output "result" {
  value = module.workspace_root.path
}
