## 插件描述

- 支持运用百度AI进行图像处理
- 支持运用stable diffusion webui进行图像处理
- 支持运用stable diffusion webui画图，不影响dall-3画图
- 支持运用suno音乐组合AI进行图生音，文生音
- 支持运用AI进行文件总结，图片总结等
- 支持多种stable diffusion模型
- 支持管理员控制群聊图像，文件，音乐，更改群聊模型等功能
- 支持并发控制，管理员参数控制
- 支持stable diffusion图生图，文生图自定义模板
- 支持企业微信，个人号，公众号部署


### 1.使用前先安装stable diffusion webui，并在它的启动参数中添加 "--api",并开启**种子数**。

* 安装具体信息，请参考[视频](https://www.youtube.com/watch?v=Z6FmiaWBbAE&t=3s)。
* 部署运行后，保证主机能够成功访问http://127.0.0.1:7860/
* 如果是服务器部署则不必需要内网穿透，如果是本地电脑部署推荐[cpolar](https://dashboard.cpolar.com/signup)启动内网穿透

#### **如下图**

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/7c58fde5-832c-4e8d-b822-0117cd77814f)

#### **请确保图片的文件名字有种子数进行命名**

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/5e310369-011d-430c-a85b-ca95946af799)

### 2.**确保图片位置填写正确**

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/7736b31e-c58c-47b0-8f44-0dc167d43027)

```
"file_url": "file=D:/sd/sd-webui-aki/sd-webui-aki-v4.2/sd-webui-aki-v4.2/outputs/,  #这个地址是你图片生成的地址"
```

### 3. 请确保**安装**本插件的依赖包```pip3 install -r requireents.txt```

```
pip3 install -r requirements.txt
```


```config.json
# config.json文件内容示例
{
    # 是否使用pictureChange插件功能
    "use_pictureChange": true,
    # 是否使用SD功能
    "use_stable_diffusion": false,
    # 是否开启Suno音乐功能
    "use_music_handle": true,
    # 是否开启文件识别功能
    "use_file_handle": true,
    # 是否开启群聊管理功能
    "use_group_handle": true,
    # Stable Diffusion 最大并发数
    "max_number": 3,
    # 触发suno音乐关键词
    "music_create_prefix": [
        "唱",
        "帮我唱"
    ],
    # 触发SD画图关键词
    "image_create_prefix": [
        "SD画",
        "SD帮我画"
    ],
    # 是否使用翻译提示词，否的话使用当前对话机器人进行翻译
    "is_use_fanyi": false,
    # 百度翻译API密钥
    "baidu_api_key": "0fqG8crG04FDU",
    # 百度翻译API密钥
    "baidu_secret_key": "RQXZgD9j7hZqgse",
    # 外部识别图片和文件或者suno音乐的API BASE URL
    "openai_api_base": "https://xxx/v1",
    # 外部识别图片和文件或者suno音乐的API密钥
    "openai_api_key": "sk-8toj6An",
    "music_model": "suno-v3.5",
    # 识别图片的模型
    "image_recognize_model": "gpt-4o",
    # 识别文件的模型
    "file_recognize_model": "gpt-4o",
    # 识别图片的提示词
    "image_recognize_prompt": "请帮我描述这个图片的内容。【重要】1.请不要用markdown语法输出 2.请仔细阅读之后把你描述的内容分析给我！",
    # 识别文件的提示词
    "file_recognize_prompt": "请帮我描述这个文件的内容，【重要】1.请不要用markdown语法输出 2.请仔细阅读之后把你描述的内容分析给我！",
    # 识别图片的提示词
    "image_music_prompt": "请帮我描述这个图片的内容,将这段内容按照语义分成 Title（题目），Song Description（歌曲描述），Type of Music（音乐类型）。并根据用户的意图生成对应语言的歌曲提示词。请直接了当地输出Title（题目），Song Description（歌曲描述），Type of Music（音乐类型），[重点]不要超过100字！！！",
    # 图生图最大尺寸
    "max_size": 1024,
    # SD启动参数
    "start": {
        "host": "127.0.0.1",
        "port": 7860,
        "use_https": false
    },
    # 本地SD图片存放位置
    "file_url": "file=G:/sd/sd-webui-aki-v4.8/outputs/",
    # 默认参数
    "defaults": {
        "params": {
            "sampler_name": "Euler a",
            "steps": 20,
            "width": 1024,
            "height": 1024,
            "cfg_scale": 7,
            "prompt": "absurdres, 8k",
            "negative_prompt": "(((nsfw))),EasyNegative,badhandv4,ng_deepnegative_v1_75t,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), bad anatomy,DeepNegative, skin spots, acnes, skin blemishes,(fat:1.2),facing away, looking away,tilted head, lowres,bad anatomy,bad hands, missing fingers,extra digit, fewer digits,bad feet,poorly drawn hands,poorly drawn face,mutation,deformed,extra fingers,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,teethcroppe,signature, watermark, username,blurry,cropped,jpeg artifacts,text,error,Lower body exposure",
            "enable_hr": false,
            "hr_scale": 2,
            "hr_upscaler": "Latent",
            "hr_second_pass_steps": 15,
            "denoising_strength": 0.7
        },
        "options": {
            "sd_model_checkpoint": "anything-v5-PrtRE.safetensors [7f96a1a9ca]"
        }
    },
    "rules": [
        {
            "keywords": [
                "横版",
                "壁纸"
            ],
            "params": {
                "width": 640,
                "height": 384
            },
            "desc": "分辨率会变成640x384"
        },
        {
            "keywords": [
                "竖版"
            ],
            "params": {
                "width": 384,
                "height": 640
            },
            "desc": "分辨率会变成384x640"
        },
        {
            "keywords": [
                "高清"
            ],
            "params": {
                "enable_hr": true,
                "hr_scale": 1.4
            },
            "desc": "出图分辨率长宽都会提高1.4倍"
        },
        {
            "keywords": [
                "二次元"
            ],
            # 切换模型
            "options": {
                "sd_model_checkpoint": "anything-v5-PrtRE.safetensors [7f96a1a9ca]"
            },
            "desc": "使用二次元风格模型出图"
        },
        {
            "keywords": [
                "现实"
            ],
            # 切换模型
            "options": {
                "sd_model_checkpoint": "absolutereality_v181.safetensors [463d6a9fe8]"
            },
            "desc": "使用现实风格模型出图"
        }
    ],
    # 可自定义图生图角色
    "roles": [
        {
            "title": "👧 可爱女生",
            "enable": false,
            "prompt": "multiple girls,Masterpiece,best quality, <lora:cozy anime_20230630155224:1>",
            "negative_prompt": "(((nsfw))),EasyNegative,badhandv4,ng_deepnegative_v1_75t,(worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), bad anatomy,DeepNegative, skin spots, acnes, skin blemishes,(fat:1.2),facing away, looking away,tilted head, lowres,bad anatomy,bad hands, missing fingers,extra digit, fewer digits,bad feet,poorly drawn hands,poorly drawn face,mutation,deformed,extra fingers,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,teethcroppe,signature, watermark, username,blurry,cropped,jpeg artifacts,text,error,Lower body exposure",
            "denoising_strength": 0.5,
            "cfg_scale": 7.0,
            "options": {
                "sd_model_checkpoint": "anything-v5-PrtRE.safetensors [7f96a1a9ca]"
            }
        },
        {
            "title": "🧑 帅气男神",
            "enable": true,
            "prompt": "multiple boys, male focus, topless male, messy hair, looking at viewer, outdoors, beautiful lighting, deep shadow, best quality, masterpiece, ultra highres, photorealistic, blurry background,",
            "negative_prompt": "cartoon, anime, sketches,(worst quality, low quality), (deformed, distorted, disfigured), (bad eyes, wrong lips, weird mouth, bad teeth, mutated hands and fingers:1.2), bad anatomy, wrong anatomy, amputation, extra limb, missing limb, floating limbs, disconnected limbs, mutation, ugly, disgusting, (bad_pictures, negative_hand-neg:1.2)",
            "denoising_strength": 0.45,
            "cfg_scale": 8.0,
            "options": {
                "sd_model_checkpoint": "anything-v5-PrtRE.safetensors [7f96a1a9ca]"
            }
        }
    ]
}

```


- groupService/config.json

```groupService/config.json
{
    # 控制群聊的功能
    "AllFunction": {
        # 是否进行图片处理
        "IS_IMAGE": "True",
        # 是否进行文件处理
        "IS_FILE": "True",
        # 是否进行音乐处理
        "IS_MUSIC": "True",
        # 群聊可用模型列表
        "MODEL": [
            "gpt-4o",
            "glm-4",
            "abab6.5-chat",
            "abab6.5s-chat"
        ]
    },
    "group": [
        {
            # 群聊名称
            "name": "500 Not Found",
            "function": {
                "IMAGE": "True",
                "FILE": "True",
                "MUSIC": "True",
                "MODEL": "abab6.5s-chat",
                "发送消息": "True"
            }
        }
    ]
}
```

- adminService/config.json
```adminService/config.json
{
    "admin_id": [],
    "admin_password": "xxx"
}
```

<details>
<summary>

    使用实例
</summary>


#### 图生图

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/4d6f16b0-136a-48d6-991e-482ce3bbc701)

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/783d6f22-c18e-4368-bc91-aa62a24c0c78)

![9d3c926daec3b69ef1f2e1b38e4ad7e](https://github.com/Yanyutin753/pictureChange/assets/132346501/cc5f8843-6a42-422c-bbeb-1c073ffa651b)

#### 画图

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/428a2333-1589-42fd-88df-a1b182f8b3f6)

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/89782b7c-8f28-42af-8c16-a588539219a3)

#### 支持放大 变换操作

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/1ab662b2-bd3c-490f-9981-404dcb1ca0e3)

![image](https://github.com/Yanyutin753/pictureChange/assets/132346501/32949ac2-93fc-4b7c-8387-f5cd7b1cb139)

#### suno音乐
  
- 1. 文生图
![ff731f85a945cac88772af6f2cad790](https://github.com/Yanyutin753/pictureChange/assets/132346501/dde5488a-d9b2-4c71-b971-28074a477db1)

- 2. 图生图
![d2f549aec32642e0ff2dbc9ad4f8956](https://github.com/Yanyutin753/pictureChange/assets/132346501/264ede7d-e162-423b-b9d3-2cb145fd4cd5)

#### 文件识别
![dd0b8389d12a753f37781259c0f6ea7](https://github.com/Yanyutin753/pictureChange/assets/132346501/d973d5ce-b228-4d98-8771-7ffddccaecb1)

#### 图片识别
![cf7e611c93f674098a3752f4f720a93](https://github.com/Yanyutin753/pictureChange/assets/132346501/94c171e4-2a96-4553-be82-998b39a962a5)

#### 群聊管理和config管理
![8f911097129cb2585526e75556f4182](https://github.com/Yanyutin753/pictureChange/assets/132346501/1597cef7-d72c-4850-b3da-5978e759a21a)


</details>
   
### 贡献与支持

- 欢迎贡献代码，提出问题和建议。如果你发现了bug或者有新的功能想法，请提交一个Issue让我知道。你也可以通过Fork项目并提交Pull
  Request来贡献代码。 如果你想部署这个项目，给我一个星星⭐，这是对我最大的支持！
- 敲代码不易，希望客官给点赞助，让我更好修改代码！
  ![image](https://github.com/Yanyutin753/wechat_pictureChange/assets/132346501/713eb69e-6e00-46ad-bec5-0b3926305ef0)



