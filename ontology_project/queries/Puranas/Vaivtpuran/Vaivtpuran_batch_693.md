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

### Verse 1 (Vaivtpuran 123.19337)
- **Original**: अस्माक स्तवने यस्य ध्रूभड्रश्च॒सुदुर्लभ:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 123.19338)
- **Original**: तबैव॒ भर्त्सने. भीतश्चावयोरन्तरं हरि:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 123.19339)
- **Original**: इति औब्रह्मवैवर्ते ब्रह्मेशशेषादिकृतं औद्रधास्तोत्र सम्पूर्णमू। ( श्रीकृष्णजन्मखण्ड 123
- **Translation**: 

---

### Verse 4 (Vaivtpuran 123.19340)
- **Original**: 98-107) #3##000-* 4 972000000 महें श्वर उवाच श्रीजगन्मड्गलस्थास्थ कब॒चस्य प्रजापति:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 123.19341)
- **Original**: ऋषिश्ठन्दो5स्य गायत्री देवी रासेश्वरी स्वयम्‌। श्रीकृष्णभक्तिसम्प्राप्ता॑ विनियोग: प्रकीर्तित:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 123.19342)
- **Original**: शिष्याय कृष्णभक्ताय ब्राह्मणाय प्रकाशयेत्‌। शठाय परशिष्याय दत्त्वा मृत्युमवाघ्रुयात्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 123.19343)
- **Original**: राज्यं देयं शिरों देयं न देयं कवचं प्रिये। कण्ठे धृतमिर्द भक्त्या कृष्णेन परमात्मना
- **Translation**: 

---

### Verse 8 (Vaivtpuran 123.19344)
- **Original**: मया दृष्ट च गोलोके ब्रह्मणा विष्णुना पुरा। 30 राधेति चतुर्श्यन्त॑बह्लिजायान्तमेव च
- **Translation**: 

---

### Verse 9 (Vaivtpuran 123.19345)
- **Original**: कृष्णेनोपासितों मन्त्र: कल्पवृक्ष: शिरोउवतु। 30 हीं श्रीं राधिकाडेन्तं बढ्लिजायान्तमेब च
- **Translation**: 

---

### Verse 10 (Vaivtpuran 123.19346)
- **Original**: कपालं नेत्रयुग्प॑च॒ श्रोत्रयुग्म॑ सदायतु
- **Translation**: 

---

### Verse 11 (Vaivtpuran 123.19347)
- **Original**: 30 रां हीं श्रीं राधिकेति डेन्तं बह्लिजायान्तमेज च
- **Translation**: 

---

### Verse 12 (Vaivtpuran 123.19348)
- **Original**: मस्तक॑ केशसंघांश्च मन्त्रराज: सदाबतु । 37 रां राधेति चतुर्थ्यन्त॑ बह्लिजायान्तमेव च
- **Translation**: 

---

### Verse 13 (Vaivtpuran 123.19349)
- **Original**: सर्वसिद्ध्धिप्रद: पातु कपोल नासिकां मुखम्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 123.19350)
- **Original**: क्लीं श्रीं कृष्णप्रियाडेन्तं कण्ठं पातु नमोउन्तकम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 265.5011)
- **Original**: + प्रकृतिखण्ड 265 02 2 2 2. 2 3 3.
- **Translation**: 

---

### Verse 16 (Vaivtpuran 265.5012)
- **Original**: ) 2 ]0)0 00000 00 0 080) 0)
- **Translation**: 

---

### Verse 17 (Vaivtpuran 265.5013)
- **Original**: । ब्रह्मपुत्र आदि सब लोग ब्रह्मलोकमें चले जाते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 265.5014)
- **Original**: संहार करके स्वयं श्रीकृष्णके वक्ष:स्थलमें विलीन हैं। दैनन्दिन प्रलय व्यतीत होनेपर ब्रह्माजी पुनः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 265.5015)
- **Original**: हो जाती है। संतपुरुष उसीको सनातनी विष्णुमाया, लोकोंकी सृष्टि आरम्भ करते हैं। इस प्रकार सौ सर्वशक्तिस्वरूपा दुर्गा, सती नारायणी, श्रीकृष्णकी वर्षोंतक ब्रह्माकी आयु पूरी होती है। तदनन्तर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 265.5016)
- **Original**: बुद्धिकी अधिष्ठात्री देवी तथा निर्गुणात्मिका कहते ब्रह्माजीकी आयु पूर्ण होनेपर एक कल्प पूरा हो
- **Translation**: 

---

