
variable "targets" {
  type        = list(string)
  description = "List of files or directories to search for"
}

variable "cwd" {
  type     = string
  nullable = true
  default  = null
}
