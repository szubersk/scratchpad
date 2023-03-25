package main

import future.keywords.every
import data.config as config


has_key(map, key) {
	_ = map[key]
}

has_keys_only(map, key_list) {
  every k, _ in map {
    _ = key_list[k]
  }
}

roles[role] {
	role := input.Roles[_]
	not contains(role.Arn, "/aws-reserved/")
	not contains(role.Arn, "/aws-service-role/")
}

statements := {arn: statements |
  r := roles[_]
  arn := r.Arn
	statements := r.AssumeRolePolicyDocument.Statement
}

deny[msg] {
	r := roles[_]

	r.MaxSessionDuration > config.max_session_duration

	msg := sprintf(
		"'%s': maximum session duration cannot be longer than %d (%d)",
		[r.Arn, config.max_session_duration, r.MaxSessionDuration],
	)
}

deny[msg] {
	r := roles[_]

  version := r.AssumeRolePolicyDocument.Version
	version != "2012-10-17"

	msg := sprintf(
		"'%s': old policy version (%s), should be '2012-10-17'",
		[r.Arn, version],
	)
}

deny[msg] {
  some arn
  action := statements[arn][_].Action

  action != "sts:AssumeRole"

	msg := sprintf(
		"'%s': Action should be 'sts:AssumeRole' (%s)",
		[arn, action],
	)
}

deny[msg] {
	some arn
	effect := statements[arn][_].Effect

	effect != "Allow"

	msg := sprintf(
		"'%s': Effect should be 'Allow' (%s)",
		[arn, effect],
	)
}

deny[msg] {
	some arn
	principal := statements[arn][_].Principal

	not has_keys_only(principal, config.allowed_principal_types)

	msg := sprintf(
		"'%s': Principal should be one of %s (%s)",
		[arn, config.allowed_principal_types, principal],
	)
}

deny[msg] {
	some arn
	aws := statements[arn][_].Principal.AWS

	not has_key(config.allowed_aws_principals, aws)

	msg := sprintf(
		"'%s': Principal should be one of %s (%s)",
		[arn, config.allowed_aws_principals, aws],
	)
}
