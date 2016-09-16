import datetime

ephemerisTestISSPass1_1Sec  =  [('2014-04-25 00:47:50',  0.8539,  0.3238, 0),
                                ('2014-04-25 00:47:50',  0.9622,  0.3664, 0),
                                ('2014-04-25 00:47:51',  1.0711,  0.4091, 0),
                                ('2014-04-25 00:47:52',  1.1806,  0.4521, 0),
                                ('2014-04-25 00:47:53',  1.2905,  0.4952, 0),
                                ('2014-04-25 00:47:55',  1.4010,  0.5385, 0),
                                ('2014-04-25 00:47:56',  1.5121,  0.5819, 0),
                                ('2014-04-25 00:47:57',  1.6237,  0.6256, 0),
                                ('2014-04-25 00:47:58',  1.7358,  0.6694, 0),
                                ('2014-04-25 00:47:58',  1.8485,  0.7134, 0),
                                ('2014-04-25 00:47:59',  1.9618,  0.7576, 0),
                                ('2014-04-25 00:48:00',  2.0756,  0.8020, 0),
                                ('2014-04-25 00:48:02',  2.1899,  0.8465, 0),
                                ('2014-04-25 00:48:03',  2.3049,  0.8912, 0),
                                ('2014-04-25 00:48:04',  2.4204,  0.9361, 0),
                                ('2014-04-25 00:48:05',  2.5365,  0.9812, 0),
                                ('2014-04-25 00:48:05',  2.6531,  1.0264, 0),
                                ('2014-04-25 00:48:06',  2.7704,  1.0718, 0),
                                ('2014-04-25 00:48:07',  2.8882,  1.1174, 0),
                                ('2014-04-25 00:48:08',  3.0066,  1.1632, 0),
                                ('2014-04-25 00:48:10',  3.1257,  1.2091, 0),
                                ('2014-04-25 00:48:11',  3.2453,  1.2552, 0),
                                ('2014-04-25 00:48:12',  3.3655,  1.3014, 0),
                                ('2014-04-25 00:48:12',  3.4863,  1.3478, 0),
                                ('2014-04-25 00:48:13',  3.6077,  1.3943, 0),
                                ('2014-04-25 00:48:14',  3.7297,  1.4410, 0),
                                ('2014-04-25 00:48:15',  3.8524,  1.4879, 0),
                                ('2014-04-25 00:48:17',  3.9757,  1.5349, 0),
                                ('2014-04-25 00:48:18',  4.0995,  1.5821, 0),
                                ('2014-04-25 00:48:19',  4.2241,  1.6294, 0),
                                ('2014-04-25 00:48:20',  4.3492,  1.6768, 0),
                                ('2014-04-25 00:48:20',  4.4750,  1.7244, 0),
                                ('2014-04-25 00:48:21',  4.6014,  1.7721, 0),
                                ('2014-04-25 00:48:22',  4.7285,  1.8200, 0),
                                ('2014-04-25 00:48:24',  4.8562,  1.8680, 0),
                                ('2014-04-25 00:48:25',  4.9845,  1.9161, 0),
                                ('2014-04-25 00:48:26',  5.1135,  1.9644, 0),
                                ('2014-04-25 00:48:27',  5.2432,  2.0128, 0),
                                ('2014-04-25 00:48:27',  5.3736,  2.0613, 0),
                                ('2014-04-25 00:48:28',  5.5046,  2.1099, 0),
                                ('2014-04-25 00:48:29',  5.6362,  2.1586, 0),
                                ('2014-04-25 00:48:30',  5.7686,  2.2075, 0),
                                ('2014-04-25 00:48:32',  5.9016,  2.2565, 0),
                                ('2014-04-25 00:48:33',  6.0353,  2.3056, 0),
                                ('2014-04-25 00:48:34',  6.1697,  2.3548, 0),
                                ('2014-04-25 00:48:35',  6.3048,  2.4041, 0),
                                ('2014-04-25 00:48:35',  6.4406,  2.4535, 0),
                                ('2014-04-25 00:48:36',  6.5770,  2.5031, 0),
                                ('2014-04-25 00:48:37',  6.7142,  2.5527, 0),
                                ('2014-04-25 00:48:39',  6.8521,  2.6025, 0),
                                ('2014-04-25 00:48:40',  6.9907,  2.6523, 0),
                                ('2014-04-25 00:48:41',  7.1300,  2.7022, 0),
                                ('2014-04-25 00:48:42',  7.2701,  2.7523, 0),
                                ('2014-04-25 00:48:42',  7.4108,  2.8024, 0),
                                ('2014-04-25 00:48:43',  7.5523,  2.8526, 0),
                                ('2014-04-25 00:48:44',  7.6946,  2.9029, 0),
                                ('2014-04-25 00:48:45',  7.8375,  2.9533, 0),
                                ('2014-04-25 00:48:47',  7.9812,  3.0038, 0),
                                ('2014-04-25 00:48:48',  8.1257,  3.0543, 0),
                                ('2014-04-25 00:48:49',  8.2709,  3.1050, 0),
                                ('2014-04-25 00:48:49',  8.4168,  3.1557, 0),
                                ('2014-04-25 00:48:50',  8.5636,  3.2065, 0),
                                ('2014-04-25 00:48:51',  8.7110,  3.2574, 0),
                                ('2014-04-25 00:48:52',  8.8593,  3.3083, 0),
                                ('2014-04-25 00:48:54',  9.0083,  3.3593, 0),
                                ('2014-04-25 00:48:55',  9.1581,  3.4104, 0),
                                ('2014-04-25 00:48:56',  9.3087,  3.4616, 0),
                                ('2014-04-25 00:48:57',  9.4600,  3.5128, 0),
                                ('2014-04-25 00:48:57',  9.6122,  3.5641, 0),
                                ('2014-04-25 00:48:58',  9.7651,  3.6155, 0),
                                ('2014-04-25 00:48:59',  9.9189,  3.6669, 0),
                                ('2014-04-25 00:49:00', 10.0734,  3.7184, 0),
                                ('2014-04-25 00:49:02', 10.2288,  3.7699, 0),
                                ('2014-04-25 00:49:03', 10.3849,  3.8215, 0),
                                ('2014-04-25 00:49:04', 10.5419,  3.8731, 0),
                                ('2014-04-25 00:49:04', 10.6997,  3.9248, 0),
                                ('2014-04-25 00:49:05', 10.8583,  3.9765, 0),
                                ('2014-04-25 00:49:06', 11.0178,  4.0283, 0),
                                ('2014-04-25 00:49:07', 11.1781,  4.0802, 0),
                                ('2014-04-25 00:49:09', 11.3392,  4.1320, 0),
                                ('2014-04-25 00:49:10', 11.5012,  4.1840, 0),
                                ('2014-04-25 00:49:11', 11.6640,  4.2359, 0),
                                ('2014-04-25 00:49:12', 11.8276,  4.2879, 0),
                                ('2014-04-25 00:49:12', 11.9921,  4.3399, 0),
                                ('2014-04-25 00:49:13', 12.1575,  4.3920, 0),
                                ('2014-04-25 00:49:14', 12.3238,  4.4441, 0),
                                ('2014-04-25 00:49:16', 12.4909,  4.4962, 0),
                                ('2014-04-25 00:49:17', 12.6589,  4.5484, 0),
                                ('2014-04-25 00:49:18', 12.8277,  4.6006, 0),
                                ('2014-04-25 00:49:19', 12.9975,  4.6528, 0),
                                ('2014-04-25 00:49:19', 13.1681,  4.7050, 0),
                                ('2014-04-25 00:49:20', 13.3396,  4.7572, 0),
                                ('2014-04-25 00:49:21', 13.5120,  4.8095, 0),
                                ('2014-04-25 00:49:22', 13.6853,  4.8618, 0),
                                ('2014-04-25 00:49:24', 13.8595,  4.9140, 0),
                                ('2014-04-25 00:49:25', 14.0347,  4.9663, 0),
                                ('2014-04-25 00:49:26', 14.2107,  5.0186, 0),
                                ('2014-04-25 00:49:27', 14.3876,  5.0709, 0),
                                ('2014-04-25 00:49:27', 14.5655,  5.1232, 0),
                                ('2014-04-25 00:49:28', 14.7443,  5.1756, 0),
                                ('2014-04-25 00:49:29', 14.9240,  5.2279, 0),
                                ('2014-04-25 00:49:31', 15.1047,  5.2802, 0),
                                ('2014-04-25 00:49:32', 15.2863,  5.3325, 0),
                                ('2014-04-25 00:49:33', 15.4688,  5.3848, 0),
                                ('2014-04-25 00:49:34', 15.6522,  5.4370, 0),
                                ('2014-04-25 00:49:34', 15.8367,  5.4893, 0),
                                ('2014-04-25 00:49:35', 16.0220,  5.5415, 0),
                                ('2014-04-25 00:49:36', 16.2083,  5.5938, 0),
                                ('2014-04-25 00:49:37', 16.3956,  5.6460, 0),
                                ('2014-04-25 00:49:39', 16.5839,  5.6982, 0),
                                ('2014-04-25 00:49:40', 16.7731,  5.7503, 0),
                                ('2014-04-25 00:49:41', 16.9633,  5.8024, 0),
                                ('2014-04-25 00:49:41', 17.1544,  5.8545, 0),
                                ('2014-04-25 00:49:42', 17.3466,  5.9066, 0),
                                ('2014-04-25 00:49:43', 17.5397,  5.9586, 0),
                                ('2014-04-25 00:49:44', 17.7338,  6.0106, 0),
                                ('2014-04-25 00:49:46', 17.9289,  6.0625, 0),
                                ('2014-04-25 00:49:47', 18.1250,  6.1144, 0),
                                ('2014-04-25 00:49:48', 18.3220,  6.1662, 0),
                                ('2014-04-25 00:49:49', 18.5201,  6.2180, 0),
                                ('2014-04-25 00:49:49', 18.7192,  6.2697, 0),
                                ('2014-04-25 00:49:50', 18.9193,  6.3214, 0),
                                ('2014-04-25 00:49:51', 19.1204,  6.3730, 0),
                                ('2014-04-25 00:49:53', 19.3225,  6.4245, 0),
                                ('2014-04-25 00:49:54', 19.5256,  6.4760, 0),
                                ('2014-04-25 00:49:55', 19.7297,  6.5274, 0),
                                ('2014-04-25 00:49:56', 19.9349,  6.5787, 0),
                                ('2014-04-25 00:49:56', 20.1411,  6.6300, 0),
                                ('2014-04-25 00:49:57', 20.3483,  6.6811, 0),
                                ('2014-04-25 00:49:58', 20.5565,  6.7322, 0),
                                ('2014-04-25 00:49:59', 20.7658,  6.7832, 0),
                                ('2014-04-25 00:50:01', 20.9761,  6.8341, 0),
                                ('2014-04-25 00:50:02', 21.1874,  6.8849, 0),
                                ('2014-04-25 00:50:03', 21.3998,  6.9356, 0),
                                ('2014-04-25 00:50:04', 21.6132,  6.9862, 0),
                                ('2014-04-25 00:50:04', 21.8276,  7.0367, 0),
                                ('2014-04-25 00:50:05', 22.0431,  7.0871, 0),
                                ('2014-04-25 00:50:06', 22.2597,  7.1373, 0),
                                ('2014-04-25 00:50:08', 22.4773,  7.1875, 0),
                                ('2014-04-25 00:50:09', 22.6959,  7.2375, 0),
                                ('2014-04-25 00:50:10', 22.9156,  7.2874, 0),
                                ('2014-04-25 00:50:11', 23.1364,  7.3372, 0),
                                ('2014-04-25 00:50:11', 23.3582,  7.3868, 0),
                                ('2014-04-25 00:50:12', 23.5810,  7.4363, 0),
                                ('2014-04-25 00:50:13', 23.8050,  7.4857, 0),
                                ('2014-04-25 00:50:14', 24.0299,  7.5349, 0),
                                ('2014-04-25 00:50:16', 24.2560,  7.5839, 0),
                                ('2014-04-25 00:50:17', 24.4831,  7.6328, 0),
                                ('2014-04-25 00:50:18', 24.7112,  7.6816, 0),
                                ('2014-04-25 00:50:18', 24.9405,  7.7302, 0),
                                ('2014-04-25 00:50:19', 25.1708,  7.7786, 0),
                                ('2014-04-25 00:50:20', 25.4021,  7.8268, 0),
                                ('2014-04-25 00:50:21', 25.6345,  7.8749, 0),
                                ('2014-04-25 00:50:23', 25.8680,  7.9228, 0),
                                ('2014-04-25 00:50:24', 26.1025,  7.9705, 0),
                                ('2014-04-25 00:50:25', 26.3381,  8.0180, 0),
                                ('2014-04-25 00:50:26', 26.5748,  8.0654, 0),
                                ('2014-04-25 00:50:26', 26.8125,  8.1125, 0),
                                ('2014-04-25 00:50:27', 27.0513,  8.1594, 0),
                                ('2014-04-25 00:50:28', 27.2912,  8.2061, 0),
                                ('2014-04-25 00:50:29', 27.5321,  8.2527, 0),
                                ('2014-04-25 00:50:31', 27.7741,  8.2989, 0),
                                ('2014-04-25 00:50:32', 28.0171,  8.3450, 0),
                                ('2014-04-25 00:50:33', 28.2612,  8.3909, 0),
                                ('2014-04-25 00:50:33', 28.5063,  8.4365, 0),
                                ('2014-04-25 00:50:34', 28.7525,  8.4818, 0),
                                ('2014-04-25 00:50:35', 28.9998,  8.5270, 0),
                                ('2014-04-25 00:50:36', 29.2481,  8.5719, 0),
                                ('2014-04-25 00:50:38', 29.4974,  8.6165, 0),
                                ('2014-04-25 00:50:39', 29.7478,  8.6609, 0),
                                ('2014-04-25 00:50:40', 29.9992,  8.7050, 0),
                                ('2014-04-25 00:50:41', 30.2517,  8.7489, 0),
                                ('2014-04-25 00:50:41', 30.5052,  8.7924, 0),
                                ('2014-04-25 00:50:42', 30.7597,  8.8357, 0),
                                ('2014-04-25 00:50:43', 31.0153,  8.8788, 0),
                                ('2014-04-25 00:50:45', 31.2719,  8.9215, 0),
                                ('2014-04-25 00:50:46', 31.5296,  8.9640, 0),
                                ('2014-04-25 00:50:47', 31.7882,  9.0061, 0),
                                ('2014-04-25 00:50:48', 32.0479,  9.0480, 0),
                                ('2014-04-25 00:50:48', 32.3085,  9.0895, 0),
                                ('2014-04-25 00:50:49', 32.5702,  9.1307, 0),
                                ('2014-04-25 00:50:50', 32.8329,  9.1716, 0),
                                ('2014-04-25 00:50:51', 33.0966,  9.2122, 0),
                                ('2014-04-25 00:50:53', 33.3613,  9.2525, 0),
                                ('2014-04-25 00:50:54', 33.6269,  9.2924, 0),
                                ('2014-04-25 00:50:55', 33.8936,  9.3320, 0),
                                ('2014-04-25 00:50:56', 34.1612,  9.3712, 0),
                                ('2014-04-25 00:50:56', 34.4298,  9.4101, 0),
                                ('2014-04-25 00:50:57', 34.6993,  9.4487, 0),
                                ('2014-04-25 00:50:58', 34.9698,  9.4868, 0),
                                ('2014-04-25 00:51:00', 35.2413,  9.5246, 0),
                                ('2014-04-25 00:51:01', 35.5137,  9.5621, 0),
                                ('2014-04-25 00:51:02', 35.7871,  9.5991, 0),
                                ('2014-04-25 00:51:03', 36.0613,  9.6358, 0),
                                ('2014-04-25 00:51:03', 36.3365,  9.6721, 0),
                                ('2014-04-25 00:51:04', 36.6127,  9.7080, 0),
                                ('2014-04-25 00:51:05', 36.8897,  9.7435, 0),
                                ('2014-04-25 00:51:06', 37.1676,  9.7786, 0),
                                ('2014-04-25 00:51:08', 37.4464,  9.8133, 0),
                                ('2014-04-25 00:51:09', 37.7261,  9.8476, 0),
                                ('2014-04-25 00:51:10', 38.0067,  9.8814, 0),
                                ('2014-04-25 00:51:10', 38.2882,  9.9149, 0),
                                ('2014-04-25 00:51:11', 38.5705,  9.9479, 0),
                                ('2014-04-25 00:51:12', 38.8536,  9.9804, 0),
                                ('2014-04-25 00:51:13', 39.1376, 10.0126, 0),
                                ('2014-04-25 00:51:15', 39.4224, 10.0443, 0),
                                ('2014-04-25 00:51:16', 39.7081, 10.0755, 0),
                                ('2014-04-25 00:51:17', 39.9945, 10.1063, 0),
                                ('2014-04-25 00:51:18', 40.2818, 10.1366, 0),
                                ('2014-04-25 00:51:18', 40.5698, 10.1665, 0),
                                ('2014-04-25 00:51:19', 40.8586, 10.1958, 0),
                                ('2014-04-25 00:51:20', 41.1482, 10.2248, 0),
                                ('2014-04-25 00:51:21', 41.4385, 10.2532, 0),
                                ('2014-04-25 00:51:23', 41.7296, 10.2811, 0),
                                ('2014-04-25 00:51:24', 42.0214, 10.3086, 0),
                                ('2014-04-25 00:51:25', 42.3139, 10.3356, 0),
                                ('2014-04-25 00:51:25', 42.6071, 10.3620, 0),
                                ('2014-04-25 00:51:26', 42.9011, 10.3880, 0),
                                ('2014-04-25 00:51:27', 43.1957, 10.4134, 0),
                                ('2014-04-25 00:51:28', 43.4909, 10.4384, 0),
                                ('2014-04-25 00:51:30', 43.7869, 10.4628, 0),
                                ('2014-04-25 00:51:31', 44.0835, 10.4867, 0),
                                ('2014-04-25 00:51:32', 44.3807, 10.5101, 0),
                                ('2014-04-25 00:51:33', 44.6785, 10.5330, 0),
                                ('2014-04-25 00:51:33', 44.9769, 10.5553, 0),
                                ('2014-04-25 00:51:34', 45.2760, 10.5771, 0),
                                ('2014-04-25 00:51:35', 45.5755, 10.5983, 0),
                                ('2014-04-25 00:51:37', 45.8757, 10.6190, 0),
                                ('2014-04-25 00:51:38', 46.1764, 10.6391, 0),
                                ('2014-04-25 00:51:39', 46.4776, 10.6587, 0),
                                ('2014-04-25 00:51:40', 46.7794, 10.6778, 0),
                                ('2014-04-25 00:51:40', 47.0817, 10.6963, 0),
                                ('2014-04-25 00:51:41', 47.3844, 10.7142, 0),
                                ('2014-04-25 00:51:42', 47.6876, 10.7315, 0),
                                ('2014-04-25 00:51:43', 47.9913, 10.7483, 0),
                                ('2014-04-25 00:51:45', 48.2954, 10.7645, 0),
                                ('2014-04-25 00:51:46', 48.6000, 10.7801, 0),
                                ('2014-04-25 00:51:47', 48.9049, 10.7952, 0),
                                ('2014-04-25 00:51:47', 49.2103, 10.8097, 0),
                                ('2014-04-25 00:51:48', 49.5160, 10.8236, 0),
                                ('2014-04-25 00:51:49', 49.8221, 10.8369, 0),
                                ('2014-04-25 00:51:50', 50.1285, 10.8496, 0),
                                ('2014-04-25 00:51:52', 50.4353, 10.8617, 0),
                                ('2014-04-25 00:51:53', 50.7423, 10.8732, 0),
                                ('2014-04-25 00:51:54', 51.0497, 10.8841, 0),
                                ('2014-04-25 00:51:55', 51.3574, 10.8945, 0),
                                ('2014-04-25 00:51:55', 51.6653, 10.9042, 0),
                                ('2014-04-25 00:51:56', 51.9734, 10.9133, 0),
                                ('2014-04-25 00:51:57', 52.2818, 10.9218, 0),
                                ('2014-04-25 00:51:58', 52.5904, 10.9297, 0),
                                ('2014-04-25 00:52:00', 52.8992, 10.9371, 0),
                                ('2014-04-25 00:52:01', 53.2082, 10.9437, 0),
                                ('2014-04-25 00:52:02', 53.5173, 10.9498, 0),
                                ('2014-04-25 00:52:02', 53.8266, 10.9553, 0),
                                ('2014-04-25 00:52:03', 54.1360, 10.9602, 0),
                                ('2014-04-25 00:52:04', 54.4455, 10.9644, 0),
                                ('2014-04-25 00:52:05', 54.7551, 10.9681, 0),
                                ('2014-04-25 00:52:07', 55.0648, 10.9711, 0),
                                ('2014-04-25 00:52:08', 55.3745, 10.9735, 0),
                                ('2014-04-25 00:52:09', 55.6843, 10.9753, 0),
                                ('2014-04-25 00:52:10', 55.9940, 10.9765, 0),
                                ('2014-04-25 00:52:10', 56.3038, 10.9770, 0),
                                ('2014-04-25 00:52:10', 56.3038, 10.9770, 0),
                                ('2014-04-25 00:52:11', 56.6136, 10.9770, 0),
                                ('2014-04-25 00:52:12', 56.9233, 10.9763, 0),
                                ('2014-04-25 00:52:14', 57.2330, 10.9750, 0),
                                ('2014-04-25 00:52:15', 57.5426, 10.9731, 0),
                                ('2014-04-25 00:52:16', 57.8522, 10.9706, 0),
                                ('2014-04-25 00:52:17', 58.1616, 10.9675, 0),
                                ('2014-04-25 00:52:17', 58.4709, 10.9637, 0),
                                ('2014-04-25 00:52:18', 58.7801, 10.9594, 0),
                                ('2014-04-25 00:52:19', 59.0891, 10.9544, 0),
                                ('2014-04-25 00:52:20', 59.3980, 10.9488, 0),
                                ('2014-04-25 00:52:22', 59.7066, 10.9426, 0),
                                ('2014-04-25 00:52:23', 60.0151, 10.9358, 0),
                                ('2014-04-25 00:52:24', 60.3233, 10.9284, 0),
                                ('2014-04-25 00:52:25', 60.6313, 10.9204, 0),
                                ('2014-04-25 00:52:25', 60.9390, 10.9118, 0),
                                ('2014-04-25 00:52:26', 61.2465, 10.9026, 0),
                                ('2014-04-25 00:52:27', 61.5537, 10.8928, 0),
                                ('2014-04-25 00:52:29', 61.8605, 10.8824, 0),
                                ('2014-04-25 00:52:30', 62.1671, 10.8714, 0),
                                ('2014-04-25 00:52:31', 62.4733, 10.8598, 0),
                                ('2014-04-25 00:52:32', 62.7791, 10.8476, 0),
                                ('2014-04-25 00:52:32', 63.0845, 10.8348, 0),
                                ('2014-04-25 00:52:33', 63.3896, 10.8215, 0),
                                ('2014-04-25 00:52:34', 63.6943, 10.8075, 0),
                                ('2014-04-25 00:52:35', 63.9985, 10.7930, 0),
                                ('2014-04-25 00:52:37', 64.3023, 10.7779, 0),
                                ('2014-04-25 00:52:38', 64.6057, 10.7622, 0),
                                ('2014-04-25 00:52:39', 64.9086, 10.7459, 0),
                                ('2014-04-25 00:52:39', 65.2110, 10.7291, 0),
                                ('2014-04-25 00:52:40', 65.5129, 10.7118, 0),
                                ('2014-04-25 00:52:41', 65.8143, 10.6938, 0),
                                ('2014-04-25 00:52:42', 66.1151, 10.6753, 0),
                                ('2014-04-25 00:52:44', 66.4154, 10.6563, 0),
                                ('2014-04-25 00:52:45', 66.7152, 10.6366, 0),
                                ('2014-04-25 00:52:46', 67.0144, 10.6165, 0),
                                ('2014-04-25 00:52:47', 67.3130, 10.5958, 0),
                                ('2014-04-25 00:52:47', 67.6110, 10.5746, 0),
                                ('2014-04-25 00:52:48', 67.9084, 10.5528, 0),
                                ('2014-04-25 00:52:49', 68.2051, 10.5305, 0),
                                ('2014-04-25 00:52:50', 68.5012, 10.5077, 0),
                                ('2014-04-25 00:52:52', 68.7967, 10.4843, 0),
                                ('2014-04-25 00:52:53', 69.0915, 10.4604, 0),
                                ('2014-04-25 00:52:54', 69.3856, 10.4361, 0),
                                ('2014-04-25 00:52:54', 69.6790, 10.4112, 0),
                                ('2014-04-25 00:52:55', 69.9717, 10.3858, 0),
                                ('2014-04-25 00:52:56', 70.2637, 10.3599, 0),
                                ('2014-04-25 00:52:57', 70.5550, 10.3335, 0),
                                ('2014-04-25 00:52:59', 70.8455, 10.3066, 0),
                                ('2014-04-25 00:53:00', 71.1353, 10.2792, 0),
                                ('2014-04-25 00:53:01', 71.4243, 10.2514, 0),
                                ('2014-04-25 00:53:02', 71.7126, 10.2230, 0),
                                ('2014-04-25 00:53:02', 72.0000, 10.1942, 0),
                                ('2014-04-25 00:53:03', 72.2867, 10.1649, 0),
                                ('2014-04-25 00:53:04', 72.5725, 10.1352, 0),
                                ('2014-04-25 00:53:06', 72.8575, 10.1050, 0),
                                ('2014-04-25 00:53:07', 73.1417, 10.0744, 0),
                                ('2014-04-25 00:53:08', 73.4251, 10.0433, 0),
                                ('2014-04-25 00:53:09', 73.7076, 10.0117, 0),
                                ('2014-04-25 00:53:09', 73.9893,  9.9798, 0),
                                ('2014-04-25 00:53:10', 74.2701,  9.9473, 0),
                                ('2014-04-25 00:53:11', 74.5500,  9.9145, 0),
                                ('2014-04-25 00:53:12', 74.8290,  9.8813, 0),
                                ('2014-04-25 00:53:14', 75.1072,  9.8476, 0),
                                ('2014-04-25 00:53:15', 75.3844,  9.8135, 0),
                                ('2014-04-25 00:53:16', 75.6607,  9.7790, 0),
                                ('2014-04-25 00:53:16', 75.9362,  9.7441, 0),
                                ('2014-04-25 00:53:17', 76.2106,  9.7088, 0),
                                ('2014-04-25 00:53:18', 76.4842,  9.6731, 0),
                                ('2014-04-25 00:53:19', 76.7568,  9.6371, 0),
                                ('2014-04-25 00:53:21', 77.0285,  9.6006, 0),
                                ('2014-04-25 00:53:22', 77.2992,  9.5638, 0),
                                ('2014-04-25 00:53:23', 77.5690,  9.5266, 0),
                                ('2014-04-25 00:53:24', 77.8378,  9.4891, 0),
                                ('2014-04-25 00:53:24', 78.1056,  9.4512, 0),
                                ('2014-04-25 00:53:25', 78.3724,  9.4129, 0),
                                ('2014-04-25 00:53:26', 78.6383,  9.3743, 0),
                                ('2014-04-25 00:53:27', 78.9032,  9.3353, 0),
                                ('2014-04-25 00:53:29', 79.1671,  9.2960, 0),
                                ('2014-04-25 00:53:30', 79.4299,  9.2564, 0),
                                ('2014-04-25 00:53:31', 79.6918,  9.2164, 0),
                                ('2014-04-25 00:53:31', 79.9527,  9.1762, 0),
                                ('2014-04-25 00:53:32', 80.2125,  9.1356, 0),
                                ('2014-04-25 00:53:33', 80.4714,  9.0947, 0),
                                ('2014-04-25 00:53:34', 80.7292,  9.0535, 0),
                                ('2014-04-25 00:53:36', 80.9860,  9.0119, 0),
                                ('2014-04-25 00:53:37', 81.2417,  8.9701, 0),
                                ('2014-04-25 00:53:38', 81.4964,  8.9280, 0),
                                ('2014-04-25 00:53:39', 81.7501,  8.8857, 0),
                                ('2014-04-25 00:53:39', 82.0028,  8.8430, 0),
                                ('2014-04-25 00:53:40', 82.2544,  8.8001, 0),
                                ('2014-04-25 00:53:41', 82.5049,  8.7568, 0),
                                ('2014-04-25 00:53:43', 82.7544,  8.7134, 0),
                                ('2014-04-25 00:53:44', 83.0029,  8.6696, 0),
                                ('2014-04-25 00:53:45', 83.2503,  8.6256, 0),
                                ('2014-04-25 00:53:46', 83.4966,  8.5814, 0),
                                ('2014-04-25 00:53:46', 83.7419,  8.5369, 0),
                                ('2014-04-25 00:53:47', 83.9861,  8.4922, 0),
                                ('2014-04-25 00:53:48', 84.2293,  8.4472, 0),
                                ('2014-04-25 00:53:49', 84.4714,  8.4020, 0),
                                ('2014-04-25 00:53:51', 84.7124,  8.3566, 0),
                                ('2014-04-25 00:53:52', 84.9524,  8.3110, 0),
                                ('2014-04-25 00:53:53', 85.1913,  8.2651, 0),
                                ('2014-04-25 00:53:54', 85.4292,  8.2190, 0),
                                ('2014-04-25 00:53:54', 85.6660,  8.1728, 0),
                                ('2014-04-25 00:53:55', 85.9017,  8.1263, 0),
                                ('2014-04-25 00:53:56', 86.1363,  8.0796, 0),
                                ('2014-04-25 00:53:58', 86.3699,  8.0327, 0),
                                ('2014-04-25 00:53:59', 86.6024,  7.9857, 0),
                                ('2014-04-25 00:54:00', 86.8338,  7.9384, 0),
                                ('2014-04-25 00:54:01', 87.0642,  7.8910, 0),
                                ('2014-04-25 00:54:01', 87.2935,  7.8434, 0),
                                ('2014-04-25 00:54:02', 87.5217,  7.7956, 0),
                                ('2014-04-25 00:54:03', 87.7489,  7.7477, 0),
                                ('2014-04-25 00:54:04', 87.9750,  7.6996, 0),
                                ('2014-04-25 00:54:06', 88.2000,  7.6513, 0),
                                ('2014-04-25 00:54:07', 88.4240,  7.6029, 0),
                                ('2014-04-25 00:54:08', 88.6469,  7.5543, 0),
                                ('2014-04-25 00:54:08', 88.8688,  7.5056, 0),
                                ('2014-04-25 00:54:09', 89.0895,  7.4567, 0),
                                ('2014-04-25 00:54:10', 89.3093,  7.4077, 0),
                                ('2014-04-25 00:54:11', 89.5279,  7.3586, 0),
                                ('2014-04-25 00:54:13', 89.7456,  7.3093, 0),
                                ('2014-04-25 00:54:14', 89.9621,  7.2600, 0),
                                ('2014-04-25 00:54:15', 90.1776,  7.2104, 0),
                                ('2014-04-25 00:54:16', 90.3921,  7.1608, 0),
                                ('2014-04-25 00:54:16', 90.6055,  7.1111, 0),
                                ('2014-04-25 00:54:17', 90.8178,  7.0612, 0),
                                ('2014-04-25 00:54:18', 91.0291,  7.0112, 0),
                                ('2014-04-25 00:54:19', 91.2394,  6.9612, 0),
                                ('2014-04-25 00:54:21', 91.4486,  6.9110, 0),
                                ('2014-04-25 00:54:22', 91.6568,  6.8607, 0),
                                ('2014-04-25 00:54:23', 91.8640,  6.8104, 0),
                                ('2014-04-25 00:54:23', 92.0701,  6.7599, 0),
                                ('2014-04-25 00:54:24', 92.2752,  6.7094, 0),
                                ('2014-04-25 00:54:25', 92.4793,  6.6587, 0),
                                ('2014-04-25 00:54:26', 92.6823,  6.6080, 0),
                                ('2014-04-25 00:54:28', 92.8844,  6.5573, 0),
                                ('2014-04-25 00:54:29', 93.0854,  6.5064, 0),
                                ('2014-04-25 00:54:30', 93.2854,  6.4555, 0),
                                ('2014-04-25 00:54:31', 93.4843,  6.4045, 0),
                                ('2014-04-25 00:54:31', 93.6823,  6.3534, 0),
                                ('2014-04-25 00:54:32', 93.8793,  6.3023, 0),
                                ('2014-04-25 00:54:33', 94.0752,  6.2511, 0),
                                ('2014-04-25 00:54:35', 94.2702,  6.1999, 0),
                                ('2014-04-25 00:54:36', 94.4642,  6.1486, 0),
                                ('2014-04-25 00:54:37', 94.6572,  6.0972, 0),
                                ('2014-04-25 00:54:38', 94.8492,  6.0459, 0),
                                ('2014-04-25 00:54:38', 95.0402,  5.9944, 0),
                                ('2014-04-25 00:54:39', 95.2302,  5.9430, 0),
                                ('2014-04-25 00:54:40', 95.4192,  5.8915, 0),
                                ('2014-04-25 00:54:41', 95.6073,  5.8399, 0),
                                ('2014-04-25 00:54:43', 95.7944,  5.7883, 0),
                                ('2014-04-25 00:54:44', 95.9805,  5.7367, 0),
                                ('2014-04-25 00:54:45', 96.1657,  5.6851, 0),
                                ('2014-04-25 00:54:45', 96.3499,  5.6334, 0),
                                ('2014-04-25 00:54:46', 96.5332,  5.5818, 0),
                                ('2014-04-25 00:54:47', 96.7155,  5.5301, 0),
                                ('2014-04-25 00:54:48', 96.8968,  5.4783, 0),
                                ('2014-04-25 00:54:50', 97.0773,  5.4266, 0),
                                ('2014-04-25 00:54:51', 97.2567,  5.3749, 0),
                                ('2014-04-25 00:54:52', 97.4353,  5.3231, 0),
                                ('2014-04-25 00:54:53', 97.6129,  5.2713, 0),
                                ('2014-04-25 00:54:53', 97.7896,  5.2196, 0),
                                ('2014-04-25 00:54:54', 97.9653,  5.1678, 0),
                                ('2014-04-25 00:54:55', 98.1402,  5.1160, 0),
                                ('2014-04-25 00:54:56', 98.3141,  5.0643, 0),
                                ('2014-04-25 00:54:58', 98.4871,  5.0125, 0),
                                ('2014-04-25 00:54:59', 98.6592,  4.9607, 0),
                                ('2014-04-25 00:55:00', 98.8305,  4.9090, 0),
                                ('2014-04-25 00:55:00', 99.0008,  4.8573, 0),
                                ('2014-04-25 00:55:01', 99.1702,  4.8055, 0),
                                ('2014-04-25 00:55:02', 99.3387,  4.7538, 0),
                                ('2014-04-25 00:55:03', 99.5064,  4.7021, 0),
                                ('2014-04-25 00:55:05', 99.6732,  4.6504, 0),
                                ('2014-04-25 00:55:06', 99.8390,  4.5988, 0),
                                ('2014-04-25 00:55:07', 100.0041,  4.5472, 0),
                                ('2014-04-25 00:55:08', 100.1682,  4.4956, 0),
                                ('2014-04-25 00:55:08', 100.3315,  4.4440, 0),
                                ('2014-04-25 00:55:09', 100.4939,  4.3924, 0),
                                ('2014-04-25 00:55:10', 100.6555,  4.3409, 0),
                                ('2014-04-25 00:55:12', 100.8163,  4.2894, 0),
                                ('2014-04-25 00:55:13', 100.9761,  4.2380, 0),
                                ('2014-04-25 00:55:14', 101.1352,  4.1866, 0),
                                ('2014-04-25 00:55:15', 101.2934,  4.1352, 0),
                                ('2014-04-25 00:55:15', 101.4508,  4.0838, 0),
                                ('2014-04-25 00:55:16', 101.6073,  4.0326, 0),
                                ('2014-04-25 00:55:17', 101.7630,  3.9813, 0),
                                ('2014-04-25 00:55:18', 101.9179,  3.9301, 0),
                                ('2014-04-25 00:55:20', 102.0720,  3.8790, 0),
                                ('2014-04-25 00:55:21', 102.2253,  3.8279, 0),
                                ('2014-04-25 00:55:22', 102.3778,  3.7768, 0),
                                ('2014-04-25 00:55:23', 102.5295,  3.7258, 0),
                                ('2014-04-25 00:55:23', 102.6803,  3.6749, 0),
                                ('2014-04-25 00:55:24', 102.8304,  3.6240, 0),
                                ('2014-04-25 00:55:25', 102.9797,  3.5732, 0),
                                ('2014-04-25 00:55:27', 103.1282,  3.5224, 0),
                                ('2014-04-25 00:55:28', 103.2760,  3.4717, 0),
                                ('2014-04-25 00:55:29', 103.4229,  3.4211, 0),
                                ('2014-04-25 00:55:30', 103.5691,  3.3705, 0),
                                ('2014-04-25 00:55:30', 103.7145,  3.3200, 0),
                                ('2014-04-25 00:55:31', 103.8592,  3.2696, 0),
                                ('2014-04-25 00:55:32', 104.0031,  3.2192, 0),
                                ('2014-04-25 00:55:33', 104.1462,  3.1689, 0),
                                ('2014-04-25 00:55:35', 104.2886,  3.1187, 0),
                                ('2014-04-25 00:55:36', 104.4303,  3.0686, 0),
                                ('2014-04-25 00:55:37', 104.5712,  3.0185, 0),
                                ('2014-04-25 00:55:37', 104.7114,  2.9686, 0),
                                ('2014-04-25 00:55:38', 104.8508,  2.9187, 0),
                                ('2014-04-25 00:55:39', 104.9895,  2.8689, 0),
                                ('2014-04-25 00:55:40', 105.1275,  2.8192, 0),
                                ('2014-04-25 00:55:42', 105.2648,  2.7695, 0),
                                ('2014-04-25 00:55:43', 105.4014,  2.7200, 0),
                                ('2014-04-25 00:55:44', 105.5372,  2.6705, 0),
                                ('2014-04-25 00:55:45', 105.6723,  2.6212, 0),
                                ('2014-04-25 00:55:45', 105.8068,  2.5719, 0),
                                ('2014-04-25 00:55:46', 105.9405,  2.5228, 0),
                                ('2014-04-25 00:55:47', 106.0736,  2.4737, 0),
                                ('2014-04-25 00:55:48', 106.2059,  2.4248, 0),
                                ('2014-04-25 00:55:50', 106.3376,  2.3759, 0),
                                ('2014-04-25 00:55:51', 106.4686,  2.3272, 0),
                                ('2014-04-25 00:55:52', 106.5989,  2.2785, 0),
                                ('2014-04-25 00:55:52', 106.7285,  2.2300, 0),
                                ('2014-04-25 00:55:53', 106.8575,  2.1816, 0),
                                ('2014-04-25 00:55:54', 106.9858,  2.1333, 0),
                                ('2014-04-25 00:55:55', 107.1134,  2.0851, 0),
                                ('2014-04-25 00:55:57', 107.2404,  2.0370, 0),
                                ('2014-04-25 00:55:58', 107.3667,  1.9891, 0),
                                ('2014-04-25 00:55:59', 107.4924,  1.9413, 0),
                                ('2014-04-25 00:56:00', 107.6174,  1.8936, 0)]


ephemerisTestISSPass1_1SecCompact  =   [('2014-04-25 00:51:13', 39.1376, 10.0126, 0),
                                        ('2014-04-25 00:51:15', 39.4224, 10.0443, 0),
                                        ('2014-04-25 00:51:16', 39.7081, 10.0755, 0),
                                        ('2014-04-25 00:51:17', 39.9945, 10.1063, 0),
                                        ('2014-04-25 00:51:18', 40.2818, 10.1366, 0),
                                        ('2014-04-25 00:51:18', 40.5698, 10.1665, 0),
                                        ('2014-04-25 00:51:19', 40.8586, 10.1958, 0),
                                        ('2014-04-25 00:51:20', 41.1482, 10.2248, 0),
                                        ('2014-04-25 00:51:21', 41.4385, 10.2532, 0),
                                        ('2014-04-25 00:51:23', 41.7296, 10.2811, 0),
                                        ('2014-04-25 00:51:24', 42.0214, 10.3086, 0),
                                        ('2014-04-25 00:51:25', 42.3139, 10.3356, 0),
                                        ('2014-04-25 00:51:25', 42.6071, 10.3620, 0),
                                        ('2014-04-25 00:51:26', 42.9011, 10.3880, 0),
                                        ('2014-04-25 00:51:27', 43.1957, 10.4134, 0),
                                        ('2014-04-25 00:51:28', 43.4909, 10.4384, 0),
                                        ('2014-04-25 00:51:30', 43.7869, 10.4628, 0)]