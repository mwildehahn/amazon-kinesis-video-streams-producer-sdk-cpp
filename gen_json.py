import json

data = {}
data['GST_SAMPLE_APP'] = []

data['GST_SAMPLE_APP'].append({
	'DEFAULT_RETENTION_PERIOD_HOURS': 2,
	'DEFAULT_TIMECODE_SCALE_MILLISECONDS': 1,
    'DEFAULT_AVG_BANDWIDTH_BPS': 8388608,
    'DEFAULT_FRAGMENT_DURATION_MILLISECONDS': 2000,
    'DEFAULT_STORAGE_SIZE': 4 * 1024 * 1024,
    'DEFAULT_STREAM_FRAMERATE': 100,
    'DEFAULT_MAX_LATENCY_SECONDS': 60,
    'DEFAULT_BUFFER_DURATION_SECONDS': 120,
    'DEFAULT_REPLAY_DURATION_SECONDS': 40,
    'DEFAULT_CONNECTION_STALENESS_SECONDS': 60,
    # 'KMS_KEY_ID': "",
    # 'CONTENT_TYPE': "video/h264",
    # 'STREAMING_TYPE': 0, # Allowed values: 0: REALTIME, 1: NEAR_REAL_TIME, 2: OFFLINE
    # 'KEY_FRAME_FRAGMENTATION': "TRUE", # Allowed values: TRUE, FALSE
    # 'FRAME_TIMECODES': "TRUE", # Allowed values: TRUE, FALSE
    # 'ABSOLUTE_FRAGMENT_TIMES': "TRUE", # Allowed values: TRUE, FALSE
    # 'FRAGMENT_ACKS': "TRUE", # Allowed values: TRUE, FALSE
    # 'RESTART_ON_ERROR': "TRUE", # Allowed values: TRUE, FALSE
    # 'RECALCULATE_METRICS': "TRUE", # Allowed values: TRUE, FALSE

    #         duration<uint64_t, milli> max_latency = milliseconds::zero(),

    #         uint32_t nal_adaptation_flags = NAL_ADAPTATION_ANNEXB_NALS | NAL_ADAPTATION_ANNEXB_CPD_NALS,
    #         uint32_t frame_rate = 25,
    #         uint32_t avg_bandwidth_bps = 4 * 1024 * 1024,
    #         duration<uint64_t> buffer_duration = seconds(120),
    #         duration<uint64_t> replay_duration = seconds(40),
    #         duration<uint64_t> connection_staleness = seconds(30),
    #         string codec_id = "V_MPEG4/ISO/AVC",
    #         string track_name = "kinesis_video",
    #         const uint8_t* codecPrivateData = nullptr,
    #         uint32_t codecPrivateDataSize = 0,
    #         MKV_TRACK_INFO_TYPE track_type = MKV_TRACK_INFO_TYPE_VIDEO,
    #         const vector<uint8_t> segment_uuid = vector<uint8_t>(),
    #         const uint64_t default_track_id = DEFAULT_TRACK_ID,
    #         CONTENT_STORE_PRESSURE_POLICY contentStorePressurePolicy = CONTENT_STORE_PRESSURE_POLICY_DROP_TAIL_ITEM,
    #         CONTENT_VIEW_OVERFLOW_POLICY contentViewOverflowPolicy = CONTENT_VIEW_OVERFLOW_POLICY_DROP_UNTIL_FRAGMENT_START
})

with open('param.json', 'w') as outfile:
    json.dump(data, outfile)



#define DEFAULT_CREDENTIAL_ROTATION_SECONDS 3600
#define DEFAULT_CREDENTIAL_EXPIRATION_SECONDS 180
#define DEFAULT_AUDIO_VIDEO_DRIFT_TIMEOUT_SECOND 5