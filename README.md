# ansible-thanos

![image](https://user-images.githubusercontent.com/1196058/44577196-5cda4780-a788-11e8-956c-b045aa5f6ee5.png)

[Thanos is a highly-available metrics system](https://github.com/improbable-eng/thanos) that touts 'unlimited' storage capacity. This role is able to configure a Thanos Sidecar (uploading metrics), Thanos Query (for querying)

## Defaults
```
thanos_sidecar_log_level: "debug"
thanos_sidecar_grpc_port: 19091
thanos_sidecar_http_port: 19191
thanos_sidecar_cluster_port: 19391
thanos_sidecar_config_file: "/etc/thanos-sidecar.yaml"

thanos_compactor_log_level: "debug"
thanos_compactor_http_port: 19192
thanos_compactor_data_dir: ""
thanos_compactor_config_file: "/etc/thanos-compactor.yaml"

# Setting the following values to '0d' will disable them
# How long to retain raw samples in the bucket:
thanos_compactor_retention_raw: "0d"
# How long to retain samples of resolution 1 (5m)
thanos_compactor_retention_5m: "0d"
# How long to retain samples of resolution 2 (1h)
thanos_compactor_retention_1h: "0d"

thanos_query_log_level: "debug"
thanos_query_grpc_port: 19091
thanos_query_http_port: 19193
thanos_query_cluster_port: 19391

thanos_store_log_level: "debug"
thanos_store_grpc_port: 19091
thanos_store_http_port: 19194
thanos_store_cluster_port: 19391
thanos_store_index_cache_size: "250MB"
thanos_store_chunk_pool_size: "2GB"
thanos_store_config_file: "/etc/thanos-store.yaml"

thanos_cluster_peers_addr: ""
thanos_prometheus_url: http://localhost:9090
thanos_prometheus_data_dir: /etc/prometheus/data
thanos_s3_bucket_name: ""
thanos_s3_endpoint: ""
thanos_default_retention_period: "90d"

thanos_sidecar_enabled: True
thanos_query_enabled: False
thanos_compactor_enabled: False
thanos_store_enabled: False
```

- `thanos_sidecar_log_level` defines the log level that Thanos will run. Set to 'debug' by default.
- `thanos_sidecar_grpc_port` defines the GRPC port for the thanos sidecar cluster to communicate over.
- `thanos_sidecar_http_port` defines the HTTP port for the thanos sidecar cluster metrics.
- `thanos_sidecar_cluster_port` defines the port which the cluster will communicate over.
- `thanos_sidecar_config_file` defines where the bucket configuration file will sit. Defaults to `/etc/thanos-sidecar.yaml`.
- `thanos_compactor_log_level` defines the log level that Thanos will run. Set to 'debug' by default.
- `thanos_compactor_http_port` defines the HTTP port for the thanos compactor cluster metrics.
- `thanos_compactor_data_dir` defines the data directory where Thanos compactor will store temporary files.
- `thanos_compactor_config_file` defines where the bucket configuration file will sit. Defaults to `/etc/thanos-compactor.yaml`.
- `thanos_compactor_retention_raw` defines how long Thanos will keep raw Prometheus metrics. Defaults to `0d`, which means it is disabled.
- `thanos_compactor_retention_5m` defines how long Thanos will keep Prometheus metrics with a resolution of 5m. Defaults to `0d`, which means it is disabled.
- `thanos_compactor_retention_1d` defines how long Thanos will keep Prometheus metrics with a resolution of 1h. Defaults to `0d`, which means it is disabled.
- `thanos_query_log_level` defines the log level that Thanos will run. Set to 'debug' by default.
- `thanos_query_grpc_port` defines the GRPC port for the thanos query cluster to communicate over
- `thanos_query_http_port` defines the HTTP port for the thanos query cluster metrics
- `thanos_query_cluster_port` defines the port which the cluster will communicate over
- `thanos_store_log_level` defines the log level that Thanos will run. Set to 'debug' by default.
- `thanos_store_grpc_port` defines the GRPC port for the thanos sidecar cluster to communicate over
- `thanos_store_http_port` defines the HTTP port for the thanos sidecar cluster metrics
- `thanos_store_cluster_port` defines the port which the cluster will communicate over
- `thanos_store_index_cache_size` defines the maximum size of items held in the index cache
- `thanos_store_chunk_pool_size` defines the maximum size of concurrently allocatable bytes for chunks
- `thanos_store_config_file` defines where the bucket configuration file will sit. Defaults to `/etc/thanos-store.yaml`.
- `thanos_cluster_peers_addr` defines either a static list of IPs or a DNS name that will be used find other sidecars
- `thanos_prometheus_url` defines the URL that Thanos will use to pull metrics from
- `thanos_prometheus_data_dir` defines the data directory that Thanos will upload Prometheus blocks from.
- `thanos_s3_bucket_name` defines the name of the S3 bucket that Thanos will upload blocks to. This is **required**.
- `thanos_s3_endpoint` defines the endpoint of the S3 bucket. [This is defined in the AWS docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) and is **required**.
- `thanos_default_retention_period` defines the retention period of objects in the bucket.:w
- `thanos_sidecar_enabled`: defines whether the role should install thanos sidecar. Disabled by default.
- `thanos_query_enabled` defines whether the role should install thanos query. Disabled by default.
- `thanos_compactor_enabled` defines whether the role should install thanos compact. Disabled by default.
- `thanos_store_enabled` defines whether the role should install thanos store. Disabled by default.

