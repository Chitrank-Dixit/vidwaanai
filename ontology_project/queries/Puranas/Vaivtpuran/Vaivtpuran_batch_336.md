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

### Verse 1 (Vaivtpuran 16.3214)
- **Original**: रति, कश्यपके पास अदिति, बसिष्ठके पास और कौओंद्वारा उसका शरीर नोचा जाता है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3215)
- **Original**: अरुन्धती, गौतमके पास अहल्या, कर्दमके पास बहुत लम्बे समयतक वह कुम्भीपाक नरकमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3216)
- **Original**: देवहूति, बृहस्पतिके पास तारा, मनुके पास रहता है। फिर जगत्‌में जन्म पाकर उसका
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3217)
- **Original**: शतरूपा, अग्निके पास स्वाहा, इन्द्रके पास शची, रोगग्रस्त रहना निश्चित है। गणेशके पास पुष्टि, स्कन्दके पास देवसेना तथा तपको ही सर्वस्व माननेवाले नारद! इस
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3218)
- **Original**: धर्मके पास साध्वी मूर्ति पत्नीरूपसे शोभा पाती हैं, प्रकार कहकर देवी तुलसी चुप हो गयी। [वैसे ही तुम भी इस शझ्लुचूड़की सौभाग्यवती इतनेमें ब्रह्मेजीनी आकर कहा--शड्डूचूड़ !
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3219)
- **Original**: प्रिय बन जाओ। शह्लुचूड़की मृत्युके पश्चात्‌ तुम बज जार छ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3220)
- **Original**: पुनः गोलोकमें भगवान्‌ श्रीकृष्णके पास चली 9
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3221)
- **Original**: जाओगी और फिर वैकुण्ठमें चतुर्भुन भगवान्‌ बिष्णुको प्राप्त करोगी।* भगवान्‌ नारायण कहते हैं--नारद ! शद्भचूड़
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3222)
- **Original**: और तुलसीको इस प्रकार आशीर्वाद-रूपमें आज्ञा &
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3223)
- **Original**: देकर न्रह्माजी अपने लोकमें चले गये। तब शब्बुचूड़ने गान्धर्व-विवाहके अनुसार तुलसीको अपनी पत्नी बना लिया। उस समय स्वर्गमें दुन्दुभियाँ बजने लगीं। आकाशसे पुष्प बरसने तुम इस देवीके साथ क्‍या बातचीत कर रहे हो ?
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3224)
- **Original**: लगे। तदनन्तर शह्रुचूड़ अपने भवनमें जाकर अब गान्धर्व-विवाहके नियमानुसार इसे पत्नीरूपसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3225)
- **Original**: तुलसीके साथ आनन्दपूर्वक रहने लगा। स्वीकार कर लेना तुम्हारे लिये परम आवश्यक अपनी चिरसड्रिनी धर्मपत्नी परम सुन्दरी है; क्‍योंकि तुम पुरुषोंमें रत्न हो और यह साध्वी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3226)
- **Original**: तुलसीके साथ आनन्दमय जीवन बिताते हुए देवी भी कन्याओंमें रत्न समझी जाती है। इसके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3227)
- **Original**: राजाधिराज प्रतापी शद्भुचूड़ने दीर्घकालतक राज्य बाद ब्रह्माजीने तुलसीसे कहा--'पतिक्रते! तुम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3228)
- **Original**: किया। देवता, दानव, असुर, गन्धर्व, किन्नर और ऐसे गुणी पतिकी क्या परीक्षा करती हो? देवता,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3229)
- **Original**: राक्षष--सभी शह्लुचूड़के शासनकालमें सदा शान्त दानव और असुर-सबको कुचल डालनेकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3230)
- **Original**: रहते थे। अधिकार छिन जानेके कारण देवताओंकी इसमें शक्ति है। जिस प्रकार भगवान्‌ नारायणके स्थिति भिक्षुक-जैसी हो गयी थी। अत: वे सभी पास लक्ष्मी, श्रीकृष्णके पास राधिका, मेरे पास
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3231)
- **Original**: अत्यन्त उदास होकर ब्रह्माकी सभामें गये और सावित्री, भगवान्‌ वाराहके पास पृथ्वी, यज्ञके अपनी स्थिति बतलाकर बार-बार अत्यन्त विलाप *यः कन्यापालन॑ कृत्वा करोति विक्रयं यदि
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3232)
- **Original**: विपदा धनलोभेन कुम्भीपाक॑ स गच्छति
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3233)
- **Original**: (प्रकृतिखण्ड 16। 98) । पशात्‌ प्राप्श्यसि गोबिन्दं गोलोके पुनरेव च।चतुर्भुज॑ च वैकुण्ठे शद्भुचूडे मृते सति
- **Translation**: 

---

