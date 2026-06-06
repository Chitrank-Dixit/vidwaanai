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

### Verse 1 (Vaivtpuran 0.381)
- **Original**: वह स््रेहपूर्वक उसी तरह पतिका पालन करती सबसे श्रेष्ठ हो। शम्भो! तुम अमरत्व लाभ करो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.382)
- **Original**: है, जैसे माता उत्तम पुत्रका। पति पतित हो या और महान मृत्युज्रय हो जाओ। मेरे वरसे तुम्हें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.383)
- **Original**: अपतित, दरिद्र हो या धनवान्‌--कुलबती स्त्रीके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.384)
- **Original**: ऋऋऋ#ऋकऋ%%ऋऋ%ऋक़कऋऋऋ+/ऋ कफ 4 ऊऋऋफऋ ऋऋऊऋफऋऊऊऊक्ऊऊऊऋ़ऊर्ऊ कं कक आऋक्कऋक कक कफ क 44% फ़ कक कफ %#%# #ऋंऊऋकऋआऋऋ
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.385)
- **Original**: 20 * संक्षिप्त ब्रद्म॑वर्तपुराण * 55%941644$# 8 £4$ #$ 855 £ £ 4 ## $ 55 5 # 5 48 5 55 # 45 55 5 4 $ 55 55 $ 4 4# $$ $ 4 55 $ 5 55 5 5 4 45 4 4 $£ 5 $ 5 4 4 5 .. वही बन्धु, आश्रय और देवता है। जो नीच
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.386)
- **Original**: मड्रलमय नाम विद्यमान है, उसके करोड़ों जन्मोंका कुलमें उत्पन्न हुई हैं; जिनमें माता-पिताके बुरे [पाप निश्चय ही नष्ट हो जाता है। शील, स्वभाव और आचरणका सम्मिश्रण हुआ। . शूलधारी महादेवजीसे ऐसा कहकर भगवान्‌ है तथा जो परपुरुषोंके उपभोगमें आनेवाली हैं,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.387)
- **Original**: श्रीकृष्णने उन्हें कल्पबृक्ष-मन्त्र और मृत्युञ्रय- अवश्य वे ही स्त्रियाँ सदा पतिकी निन्‍दा करती
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.388)
- **Original**: तत्त्वज्ञान दिया। तत्पश्चात्‌ वे सिंहवाहिनी हैं। जो पतिको हम दोनोंसे भी बढ़कर देखती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.389)
- **Original**: दुर्गसे बोले-- और समझती है, वह सती-साध्वी स्त्री गोलोकमें श्रीभगवानने कहा--वत्से ! इस समय तुम अपने स्वामीके साथ कोटि कल्पोंतक आनन्द
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.390)
- **Original**: गोलोकमें मेरे पास रहो। फिर समय आनेपर भोगती है। शिव! वह वैष्णवी प्रकृति शिवप्रिया
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.391)
- **Original**: कल्याणके आश्रयभूत मड़लदाता शिवको पतिरूपमें होकर तुम्हारे लिये कल्याणमयी होगी। अतः मेरी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.392)
- **Original**: प्राप्त करोगी। सुमुखि! सम्पूर्ण देवताओंके आज्ञासे लोक-कल्याणके निमित्त उस साध्वीको
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.393)
- **Original**: तेज:पुझसे प्रकट हो समस्त दैत्योंका संहार करके भार्यरूपसे ग्रहण करो। तुम सबके द्वारा पूजित होओगी। तदनन्तर कल्प- तदनन्तर भगवान्‌ श्रीकृष्णने शिवलिज्अके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.394)
- **Original**: विशेषमें सत्ययुग आनेपर तुम दक्षकन्या सती स्थापन और पूजनका महान्‌ फल बतलाते हुए
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.395)
- **Original**: होओगी और शिवकी सुशीला गृहिणी बनोगी। कहा--जो “महादेव', “महादेव” और “महादेव”
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.396)
- **Original**: फिर यज्ञमें अपने स्वामीकी निन्‍्दा सुनकर का उच्चारण करता है, उसके पीछे मैं उस नाम-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.397)
- **Original**: शरीरका त्याग कर दोगी और हिमवान्‌की पत्नी श्रवणके लोभसे अत्यन्त भयभीतकी भाँति जाता
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.398)
- **Original**: मेनाके गर्भसे जन्म लेकर पार्वती नामसे विख्यात हूँ। जो मनुष्य 'शिव' शब्दका उच्चारण करके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.399)
- **Original**: होओगी। उस समय सहस्त्र दिव्य वर्षोतक तुम प्राणोंका परित्याग करता है, वह कोटि जन्मोंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.400)
- **Original**: शिवके साथ बिहार करोगी। तत्पश्चात्‌ तुम उपार्जित पापसे मुक्त हो मोक्ष प्राप्त कर लेता है।
- **Translation**: 

---

