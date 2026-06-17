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

### Verse 1 (Vaivtpuran 113.19007)
- **Original**: अधुना मम पुत्रोडई्यं बाण: शंकरकिद्भुरः: । आराच्य रक्षितः: सो5पि तेनैव भक्तबन्धुना
- **Translation**: 

---

### Verse 2 (Vaivtpuran 113.19008)
- **Original**: परिपुष्टश्न॒ पार्वत्या यथा मात्रा सुतस्तथा । गृहीतवांश्ष तत्कन्यां बलेन युवर्ती सतीमू
- **Translation**: 

---

### Verse 3 (Vaivtpuran 113.19009)
- **Original**: समुझतश्च॒तं हन्तुं कार्तिकेनापि बारितः
- **Translation**: 

---

### Verse 4 (Vaivtpuran 113.19010)
- **Original**: आगतोउसि पुन्हन्तुं पौत्रस्य दमने क्षमम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 113.19011)
- **Original**: सर्वात्पनक्ष सर्वत्र समभाव: श्रुतौँ श्रुतः। करोषि जगतां नाथ कथ्चमेव॑ व्यतिक्रमम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 113.19012)
- **Original**: त्ववा चनिहतो यो हि तस्य को रक्षिता भुवि । सुदर्शनस्थ तेजो हि सूर्यकोटिनिभं परम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 113.19013)
- **Original**: केषां सुराणामस्वेण ._ तदेवमनिवारितम्‌ । यथा सुदर्शन चैवमस्त्राणां प्रवर॑ बरम्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 113.19014)
- **Original**: तथा भवश्च देवानां सर्वेषामीश्वरः: परः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 113.19015)
- **Original**: यथा भवस्तथा कृष्णो बिधाता वेधसामपि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 113.19016)
- **Original**: विष्णु: सत्त्वगगुणाधार: शिव: सत्त्चाभ्रबस्तथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 113.19017)
- **Original**: स्वयं विधाता रजस: सृष्टिकर्ता पितामहः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 113.19018)
- **Original**: कालाग्रिरुद्रों भगवान्‌. विश्वसंहारकारकः । तमसश्चाश्रय: सो5पि रुद्राणां प्रवरों महान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 113.19019)
- **Original**: स॒एव शंकरांशश्वाप्यन्ये रुद्राआ तत्कला: । भवांक्ष निर्गुणस्तेषां प्रकृतेश्च॒ परस्तथा
- **Translation**: 

---

### Verse 14 (Vaivtpuran 113.19020)
- **Original**: सर्वेषां परमात्मा वै प्राणा विष्णुस्वरूपिण:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 113.19021)
- **Original**: मानसं लव स्वयं ब्रह्मा स्वयं ज्ानात्मक: शिव:ः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 113.19022)
- **Original**: प्रवरा सर्वशक्तीनां बुद्धिः प्रकृतिरीश्वरी । स्वात्मनः प्रतिबिम्बस्ते जीवः सर्वेषु देहिषु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 113.19023)
- **Original**: जीब: स्वकर्मणां भोगी स्वयं साक्षी भवांस्तथा । सर्वे यान्ति त्वयि गते नरदेखे यथानुगा:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 113.19024)
- **Original**: सद्य: पतति देहश्व शवोस्पृश्यस्त्वया विना । बुद्धा: सन्‍तो न जानन्ति वसद्धितास्तव मायया
- **Translation**: 

---

### Verse 19 (Vaivtpuran 113.19025)
- **Original**: त्वां भजन्त्येव ये सन्‍्तो मायापेतां तरन्ति ते। त्रिगुणा प्रकृतिर्दु्गा वैष्णबी च सनातनी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 113.19026)
- **Original**: 'परा नारायणीशानी तब माया दुरत्यया
- **Translation**: 

---

