{
  "metrics": {
    "namespace": "CustomEC2",
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "aggregation_dimensions": [
      [
        "InstanceId"
      ]
    ],
    "metrics_collected": {
      "mem": {
        "measurement": [
          {
            "name": "mem_used_percent",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60
      },
      "swap": {
        "measurement": [
          {
            "name": "swap_used_percent",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60,
        "resources": [
          "*"
        ]
      },
      "disk": {
        "measurement": [
          {
            "name": "used_percent",
            "unit": "Percent"
          }
        ],
        "ignore_file_system_types": [
          "sysfs",
          "tmpfs",
          "devtmpfs",
          "squashfs"
        ],
        "metrics_collection_interval": 60,
        "resources": [
          "*"
        ]
      }
    }
  }
}

{
  "metrics": {
    "namespace": "CustomEC2",
    "append_dimensions": {
      "InstanceId": "${aws:InstanceId}"
    },
    "aggregation_dimensions": [
      [
        "InstanceId"
      ]
    ],
    "metrics_collected": {
      "Memory": {
        "measurement": [
          {
            "name": "% Committed Bytes In Use",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60
      },
      "Paging File": {
        "measurement": [
          {
            "name": "% Usage",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60,
        "resources": [
          "*"
        ]
      },
      "LogicalDisk": {
        "measurement": [
          {
            "name": "% Free Space",
            "unit": "Percent"
          }
        ],
        "metrics_collection_interval": 60,
        "resources": [
          "*"
        ]
      }
    }
  }
}
