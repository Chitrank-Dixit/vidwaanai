# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 0.121)
- **Original**: सार-तत्त्वसे रचित किरीट-मुकुट जगमगाते रहते प्राप्तिका कारण है। योगीजन योग एबं ज्ञानदृष्टिसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.122)
- **Original**: हैं। वह श्याम-सुन्दर पुरुष रत्ममय सिंहासनपर सदा उसीका चिन्तन करते हैं। बह ज्योति ही
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.123)
- **Original**: आसीन है और आजानुलम्बिनी बनमाला उसको परमानन्ददायक, निराकार एवं परात्पर ब्रह्म है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.124)
- **Original**: शोभा बढ़ाती है। उसीको परब्रह्म परमात्मा एवं उस ब्रह्म-ज्योतिके भीतर अत्यन्त मनोहर रूप
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.125)
- **Original**: सनातन भगवान्‌ कहते हैं। वे भगवान्‌ स्वेच्छामय सुशोभित होता है, जो नूतन जलधरके समान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.126)
- **Original**: रूपधारी, सबके आदिकारण, सर्वाधार तथा श्याम है। उसके नेत्र लाल कमलके समान
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.127)
- **Original**: परात्पर परमात्मा हैं। उनकी नित्य किशोरावस्था प्रफुल्ल दिखायी देते हैं। उसका निर्मल मुख
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.128)
- **Original**: रहती है। वे सदा गोप-वेष धारण करते हैं। शरत्पूर्णिमाके चन्द्रमाकी शोभाको तिरस्कृत करनेवाला
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.129)
- **Original**: करोड़ों पूर्ण चन्द्रमाओंकी शोभासे सम्पन्न हैं तथा है। उसके रूप-लावण्यपर करोड़ों कामदेव
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.130)
- **Original**: अपने भक्तोंपर अनुग्रह करनेके लिये आकुल रहते निछावर किये जा सकते हैं। वह मनोहर रूप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.131)
- **Original**: हैं। वे ही निरीह, निर्विकार, परिपूर्णतम तथा विविध लीलाओंका धाम है। उसके दो भुजाएँ
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.132)
- **Original**: सर्वव्यापी परमेश्वर हैं तथा वे ही रासमण्डलमें हैं। एक हाथमें मुरली सुशोभित है। अधरोंपर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.133)
- **Original**: विराजमान, शान्तचित्त, परम मनोहर रासेश्वर हैं मन्द मुसकान खेलती रहती है। उसके श्रीअड्भ । मड्भलकारी, मज्गभल-योग्य, मड्रलमय तथा मज्जलदाता दिव्य रेशमी पीताम्बरसे आवृत हैं। सुन्दर रत्रमय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.134)
- **Original**: हैं; परमानन्दके बीज, सत्य, अक्षर और अविनाशी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.135)
- **Original**: * ग्रह्मखाएड + छ #
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.136)
- **Original**: %#88###8%##:# 8 89% $#% ##
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.137)
- **Original**: कक % कक #% कक कक ऋऋकऊऋऋऋककक%$% 45555 % 55% 88% हक कक कक क हैं; सम्पूर्ण सिद्धियोंके स्वामी, -सर्वसिद्धिस्वरूप
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.138)
- **Original**: परमात्मस्वरूप, शान्तर तथा सबके परम आश्रय तथा सिद्धिदाता हैं; प्रकृतिसे परे विराजमान, ईश्वर,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.139)
- **Original**: हैं। शान्तचित्त वैष्णवजन उन्हींका ध्यान करते निर्गुण, नित्य-विग्रह, आदिपुरुष और अव्यक्त हैं।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.140)
- **Original**: हैं। ऐसा उत्कृष्ट रूप धारण करनेवाले उन बहुत-से नामोंद्वार उन्हींको पुकारा जाता है।
- **Translation**: 

---

