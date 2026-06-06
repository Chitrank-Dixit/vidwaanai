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

### Verse 1 (Vishnu Puran 0.7721)
- **Original**: भीतर जानेपर भगवागने सुकुमास्को बहत्म्रती हुई घात्रीकी यह वाणों सुनी---
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7722)
- **Original**: अण् 13 ] सिंह: प्रसेनमवरधीत्सिंहो जाम्बबत्ता हतः । सुकुमारक मा रोदीस्तव ह्ोष स्थमनतक:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7723)
- **Original**: 42 इत्याकण्योपलब्धस्यमन्तकोन्त:प्रविष्ट: कुमारक्रीडनकीकृत॑ च धात्र्या हस्ते तेजोभि- जाज्वल्यमान स्यमन्तक॑ दर्दर्श
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7724)
- **Original**: ते च स्यथमन्तकाभिलपषितचक्षुषमपूर्वपुरुषमागतं समयेक्ष्य धात्री त्राहि त्राहीति व्याजहार
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7725)
- **Original**: तदारत्तरवश्रवणानन्तरें. चामर्षपूर्णददवः स जाम्बवानाजगाम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7726)
- **Original**: तयोश्वच॒ परस्पर- मुद्धतामर्षयोर्युद्धोकविंशतिदिनान्‍्यभवत्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7727)
- **Original**: ते ज यदुसैनिकास्तत्र सप्ताष्टदिनानि तन्निष्क्रान्ति- मुदीक्षमाणास्तस्थुः । 47
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7728)
- **Original**: अनिष्क्रणे च॑ म्रधुरिपुरसाववश्यमत्र बिलेउत्यन्ते नाझमखाप्तो भ्रविष्यत्यन्यथधा तस्थ जीवतः कथ्ममेताबन्ति दिनानि शन्नुजये व्याक्षेपो भविष्यतीति कृताध्य- वसाया द्वारकामागम्य हतः कृष्ण इति कथयामासु:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7729)
- **Original**: तद्ठाश्धवाश्न तत्कालोबित- मखिलपुत्तरक्रियाकल्वापं चक्कु:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7730)
- **Original**: ततश्वास्य युद्धयमानस्यातिश्रद्धादत्तविशिष्टोप- पात्रयुक्तान्नतोयादिना श्रीकृष्णस्य बलप्राण- पुष्टिसभूत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7731)
- **Original**: इतरस्थानुदिनमतिगुरुपुरुष- भरेद्यमानस्यथ अतिनिष्रप्रहारपातपीडिताखिला- सयवस्य निराहारतया बलहानिरभूत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7732)
- **Original**: निर्जितभ्न॒ भगवता जाम्बवात्रणिपत्य व्याजहार
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7733)
- **Original**: सुरासुरगन्धर्वयक्षराक्षसादिभिरप्य- खिलेभभवान्न जे्तु शक्यः किमुतावनिगोचरैरल्प- वीर्यैनरिनराववव्भूतैश्न तिर्यग्योन्यनुसृतिभि: कि पुनरस्मद्विधरवश्य॑ भवताउस्मत्स्वामिना रामेणेब नारायणस्य सकलजगत्परायणस्यांशेन भगवता भवितव्यमित्युक्तस्तस्प॑. भगवानख्िलाबनि- भारावतरणार्थमवतरणमाचचक्षे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7734)
- **Original**: प्रीत्य- भिव्यक्लितकरतलस्पर्शनेन_ चैनमपगतयुद्धखेदं चकार
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7735)
- **Original**: चतुर्थ अंज 273 सिंहने प्रसेककों मारा और सिंहक्ये जाम्बवानने; ले सुकुमार ! तू रो मत यह स्यमन्तकमणि तेरी ही है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7736)
- **Original**: यह सुननेसे स्पमन्तकका पता लगनेपर भगवानने भीतर जाकर देखा कि सुकुमारके लिये स्विल्लौना बनी हुई स्थमन्तकमणि घात्रीके हाथपर अपने तेजसे देदोप्यमान हो रही है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7737)
- **Original**: स्थमत्तकमणिकी ओर अभिलाषापूर्ण दृष्टिसे देखते हुए एक बिलक्षण पुरुषको वहाँ आया देख धात्री 'त्राहि-तआाहि' कस्के चिल्लाने लगी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7738)
- **Original**: उसकी आर्त्त-ताणीको सुनकर जाम्यवान्‌ क़्रेधपूर्ण हृदयसे वह्यँ आया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7739)
- **Original**: फिर परस्पर रोष बढ़ जानेसे उन दोनॉंका इककीस दिनतक भोर युद्ध हुआ
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7740)
- **Original**: पर्वतके पास भगवानकी प्रतोक्षा करनेवारे यादव-सैनिक सात-आठ दिनतक उनके गुफासे बाहर आनेकी बाट देखते रहे । 47
- **Translation**: 

---

