# Docker Compose

## 什麼是docker-compose

Docker Compose 是一個強大的工具，可以簡化多容器應用程式的管理。它允許您使用單一設定檔（通常名為 docker-compose.yml）定義和運行具有多個服務（容器）的複雜應用程式。此設定檔指定服務、它們的依賴項及其設置，使管理和部署應用程式變得更加容易。

## 使用 Docker Compose 的主要優點：

- 簡化管理：使用單一指令定義和管理多個容器。
- 一致的環境：確保您的應用程式在不同環境（開發、測試、生產）中一致運作。
- 更快的開發：快速啟動和拆卸應用程式堆疊以進行測試和開發。
- 改進的協作：與其他人共享應用程式的配置，從而更輕鬆地協作和重現您的設定。

## 檢查是否有安裝docker-compose

```bash
docker-compose --version
```

## 安裝docker-compose

```bash
sudo apt install docker-compose
```


## JSON格式

```json
{
    "doe": "a deer, a female deer",
    "pi": 3.14159,
    "xmas": true,
    "french-hens": 3,
    "calling-birds": [
        "huey",
        "dewey", 
        "louie",
        "fred"
    ],
    "xmas-fifth-day": {
        "calling-birds": "four",
        "french-hens": 3,
        "golden-rings": 5,
        "partridges": {
            "count": 1,
            "location": "a pear tree"
        },
        "turtle-doves": "two"
    }
}
```

## JSON轉換為YML格式
- YML的子結構是以縮排
- Array使用`-`符號表示

```yaml
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

