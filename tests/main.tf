
module "basic_usage" {
  source = "../"

  targets = ["version.txt"]
}

output "basic_usage_result" {
  value = module.basic_usage.path
}

module "multiple_files" {
  source = "../"

  targets = ["version.txt", "README.md"]
}

output "multiple_files_result" {
  value = module.multiple_files.path
}
