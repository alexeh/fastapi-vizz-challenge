# config/deploy/production.rb
server ENV['SERVER_IP'], user: 'ubuntu', roles: %w{app}

set :deploy_to, ENV['DEPLOYMENT_PATH']

set :ssh_options, {
  forward_agent: false,
  auth_methods: %w(publickey)
}
