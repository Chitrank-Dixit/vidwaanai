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

### Verse 1 (Vishnu Puran 0.12541)
- **Original**: हे मुने ! वे सर्वात्मा समस्त आवरणोंसे परे हैं। थे समस्त भूतोंकी प्रकृति, प्रकृतिके विकार तथा गुण और उनके कार्य आदि दोषोंसे विलक्षण हैं ! पृथिवी और आकाशके बीचमें जो कुछ स्थित है उन्होंने वह सब व्याप्त किया है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12542)
- **Original**: ने सम्पूर्ण कल्याण-गुणोंके स्वरूप हैं, उन्होंने अपनो मायाशक्तिके लेशमात्रसे ही सम्पूर्ण प्राणियोंकों व्याप्त किया है और वे अपनी इच्छासे स्वमनोथ्तुकूल महान्‌ दारीर धारणकर समस्त सैसारका कल्याण-साधन करते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12543)
- **Original**: वे तेज, बल, ऐश्वर्य, महाविज्ञान, बीर्य और शक्ति आदि गुणोंकी एकमात्र राशि हैं, प्रकृति आदिसे भी परे हैं और उन परावरेश्वरमें अतिद्यादि सम्पूर्ण क्लेशोंका अत्यन्ताभाव है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12544)
- **Original**: वे ईश्वर ही सर्मष्टि और व्यष्टिरूप हैं, वे ही व्यक्त और अव्यक्तस्वरूप हैं, वे ही सबके स्वामी, सबके साक्षी और सब कुछ जाननेयाले हैं तथा उन्हीं सर्वशक्तिमानकी परमेश्नरसंज्ञा है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12545)
- **Original**: जिसके द्वारा ये निर्दोष, विशुद्ध, निर्मल और एकरूप परमात्मा देस्ते या जाने जाते हैं उसीका नाम ज्ञान (पर विद्या) है और जो इसके विपरीत है वही अशञान (अपरा विद्या) है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12546)
- **Original**: ब्गनजि इति श्रीविष्णुपुराणे षष्ठेंडशे पञ्लमोज्ध्यायः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12547)
- **Original**: धाााााााकानकीमााामााक
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12548)
- **Original**: आन्द ] चष्ट अंश डेड3 छठा अध्याय केशिध्वज और खाण्डिक्यकी कथा श्रीपराइर उवाच श्रीपराशरजी बोले--वे पुरुषोत्तम स्वाध्याय और स्वाध्यायसंयमाभ्यां स दृश्यते पुरुषोत्तम: । संयमद्ारा देखे जाते हैं, ब्रह्मकी प्राप्तिका कारण होनेसे ये तत्माप्तिकारण ब्रह्म तदेतदिति पठ्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12549)
- **Original**: भी ब्रह्म ही कहल्लते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12550)
- **Original**: स्वाध्यायसे योगका और साग्यावाह्मोगवासीत योगसे स्वाध्यायका आश्रय करे । इस प्रकप्रर स्वाध्याय और स्वाध्याययोगसम्फ्त्या परः >> परमात्मा प्रकाझते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12551)
- **Original**: ढ्षते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12552)
- **Original**: बहास्वरूप परमात्माको मोसमय चक्षुओसे तदीक्षणाय स्वाध्यायश्चक्षुबोगस्तथा परम्‌।
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12553)
- **Original**: नहीं देखा जा सकता, उन्हें देखनेके लिये स्वाध्याय और न मांसचक्षूषा द्रष्ट; ब्रह्मभूतस्स शकयते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12554)
- **Original**: योग ही दो नेत्र हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12555)
- **Original**: अरमैश्रेय उवाच श्रीमैत्रेयजी बोल्छे--- भगवन्‌ ! जिसे जान लेनेपर मैं भगव॑स्तमहं योगं ज्ञातुमिच्छामि ते वद्‌। ज्ञाते यत्राखिलाधार॑ पहयेयं परमेश्वरम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12556)
- **Original**: 4 श्रीपराशर उवाच यथा केशिध्वज: प्राह खाण्डिक्याय महात्मने । जनकाय पुरा योगं तमहं कथयामि ते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12557)
- **Original**: 5 श्रीमेत्रेय उवाच खाष्डिक्य: को 5भवद्ठह्मन्को वा केशिध्बज: कृती । कर्थ तयोश्व संवादो योगसम्बन्धवानभूत्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12558)
- **Original**: 6 औफ्यदार उकाच धर्मध्वजो बै जनकस्तस्य पुत्रोडमितध्वज: । कृतध्वजश्च॒ नाम्रासीत्सदाध्यात्मरतिनप:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12559)
- **Original**: 7 कृतध्वजस्य पुत्रो3भूत्‌ ख्यात: केशिध्वजो नृप: । पुत्रोई3मितध्वजस्पापि खाण्डिक्चजनको5$भवत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12560)
- **Original**: 8 कर्ममार्गेण खाण्डिक्य: पृथिव्यामभवत्कृती । केशिध्वजो5प्यतीवासीदात्मविद्याविज्ञारद:
- **Translation**: 

---

