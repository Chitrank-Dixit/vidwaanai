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

### Verse 1 (Vaivtpuran 53.4894)
- **Original**: रहती है, पर्वत अपने स्थानपर रहते हैं और अनुग्रह किया। तुम्हें शाप नहीं दिया। तुम एक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 53.4895)
- **Original**: पाताल अपने स्थानपर। राजेन्द्र! सात स्वर्गलोक, भयानक गहरे. भवसागरमें गिर गये थे। मैंने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 53.4896)
- **Original**: सात द्वीपोंसहित पृथ्वी, पर्वत और समुद्रोंसहित तुम्हारा उद्धार किया है। केवल जलमय तीर्थ
- **Translation**: 

---

### Verse 4 (Vaivtpuran 53.4897)
- **Original**: सात पाताल--इन समस्त लोकॉसहित जो ब्रह्माण्ड ही तीर्थ नहीं है। भगवानके भक्त भी तीर्थ हैं,
- **Translation**: 

---

### Verse 5 (Vaivtpuran 53.4898)
- **Original**: है, वह अण्डेके आकारमें जलपर तैर रहा है। मिट्टी और पत्थरकी प्रतिमारूप देवता ही देवता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 53.4899)
- **Original**: प्रत्येक ब्रह्माण्डमें ब्रह्मा, विष्णु और शिव आदि नहीं हैं, भगवद्भक्त भी देवता हैं। जलमय तीर्थ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 53.4900)
- **Original**: रहते हैं। देवता, मनुष्य, नाग, गन्धर् तथा राक्षस और मिट्टी-पत्थरके देवता मनुष्यकों दीर्घकालमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 53.4901)
- **Original**: आदि निवास करते हैं। राजन! पातालसे लेकर पवित्र करते हैं; परंतु श्रीकृष्णभक्त दर्शन देनेके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 53.4902)
- **Original**: ब्रह्मलोकतक जो अण्ड है, यही ब्रह्माजीका साथ ही पवित्र कर देते हैं।* कृत्रिम ब्रह्माण्ड है। यह जलमें शयन करनेवाले राजन्‌! निकलो इस घरसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 53.4903)
- **Original**: दे दो राज्य अपने । क्षुद्र बिराटू विष्णुके नाभिकमलपर उसी तरह है पुत्रको। वत्स! अपनी साध्वी पत्नीकी रक्षाका भार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 53.4904)
- **Original**: जैसे कमलकी कर्णिकामें बीज रहा करता है। बेटेको सौंपकर शीघ्र ही बनको चलो। भूमिपाल!
- **Translation**: 

---

### Verse 12 (Vaivtpuran 53.4905)
- **Original**: . इस प्रकार सुविस्तृत जलशय्यापर शयन ब्रह्मसे लेकर कीटपर्यन्त सब कुछ मिथ्या ही है।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 53.4906)
- **Original**: करनेवाले वे प्राकृत महायोगी क्षुद्र बिराट्‌ विष्णु जो सबके ईश्वर हैं, उन परमात्मा राधावह्लभ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 53.4907)
- **Original**: भी प्रकृतिसे परवर्ती ईश्वर, सर्वात्मा, कालेश्वर श्रीकृष्णणा भजन करो। वे ध्यानसे सुलभ हैं। श्रीकृष्णका ध्यान करते हैं; उनका आधार है ब्रह्मा, विष्णु और शिव आदिके लिये भी उनकी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 53.4908)
- **Original**: महाविष्णुका विस्तृत रोमकूप। महाविष्णुके अनन्त समाराधना कठिन है। बे उत्पत्ति-विनाशशौल
- **Translation**: 

---

### Verse 16 (Vaivtpuran 53.4909)
- **Original**: रोमकूपोमेंसे प्रत्येकमें ऐसे-ऐसे ब्रह्माण्ड स्थित प्राकृत पदार्थों और प्रकृतिसे भी परे हैं। जिनकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 53.4910)
- **Original**: हैं। महाविष्णुके शरीरमें असंख्य रोम हैं और उन ही मायासे ब्रह्मा सृष्टि, विष्णु पालन तथा रुद्रदेव
- **Translation**: 

---

### Verse 18 (Vaivtpuran 53.4911)
- **Original**: रोमकूपोमें असंख्य ब्रह्माण्ड हैं। अण्डाकार ब्रह्माण्डॉंकी +ज हथ्मम्मयानि तीर्थानि न देवा मृच्छिलामया:
- **Translation**: 

---

### Verse 19 (Vaivtpuran 53.4912)
- **Original**: ते पुनन्त्युरुकालेन कृष्णभक्ताश्ष दर्शनात्‌। (प्रकृतिखण्ड 53। 25-26)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 53.4913)
- **Original**: # प्रकृतिखण्ड * 261 #ऋकऋकऋऋश् कक; ्क़कक़ कक # 6 # कक ऊअंऊऋऋऋ्कऋऋकऋ 4 ###%&##%%5%%5ऊ कक 44888 उत्पत्तिके स्थानभूत वे महाविष्णु भी सदा श्रीकृष्णकी
- **Translation**: 

---

