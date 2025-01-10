output "path" {
  value       = data.external.find_up.result.path
  description = "Firstly found file or directory given the targets and cwd"
}
