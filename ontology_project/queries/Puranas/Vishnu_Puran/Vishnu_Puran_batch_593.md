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

### Verse 1 (Vishnu Puran 0.11841)
- **Original**: अर्जुनका उद्धव क्षीण हो जानेके कारण अभिसे दिये हुए उनके अक्षय बाण भी उन अहीरोके साथ लड़नेमें नष्ट हो गये । 24
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11842)
- **Original**: तब अर्जुनने सोचा कि मैंने जो अपने रारसपृहसे अनेकों राजाओंको जीता था वह सब कृष्णचन्द्रका ही प्रभाव था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11843)
- **Original**: अर्जुनके देखते-देखते वे अहीर उन स्त्ररत्ोंकों खींच-खींचकर के जाने लगे तथा कोई- कोई अपनी इच्छानुसार इधर-उधर भाग गयीं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11844)
- **Original**: आ* 38 ] ततइशरेषु क्षीणेषु धनुष्कोट्या धनज्ञय: । जघान दस्पूंस्ते चास्य प्रहाराज्जहसुर्मुने
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11845)
- **Original**: 27 प्रेक्षतस्तस्य पार्थस्य वृष्ण्यन्धकवरस्त्रिय: । जग्मुरादाय ते म्लेच्छा: समस्ता मुनिसत्तम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11846)
- **Original**: 28 ततस्मुदु:खितो जिष्णु: कष्ट कष्टमिति ब्रुवन्‌ । अहो भगवतानेन वज्चलितोउस्मि रुरोद ह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11847)
- **Original**: 29 तद्धनुस्तानि शस्त्राणि स रथस्ते च वाजिन: । सर्वमेकपदे नष्ट दानमश्रोत्रिये यथा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11848)
- **Original**: 30 अहोउतिबलवहैव॑विना तेन महात्मना । यदसामर्थ्ययुक्तेषपि नीचवर्गे जयप्रदम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11849)
- **Original**: 31 तो बाहू स च मे मुष्टि: स्थान तत्सोउस्मि चार्जुन: । पुण्येनेव विना तेन गतं सर्वमसारताम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11850)
- **Original**: 32 ममार्जुनत्व॑ भीमस्य भीमत्वं तत्कृते धुवम्‌। बिना तेन यदाभीरैजिंतो5हं रथिनां बरः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11851)
- **Original**: 33 चकार तत्र राजानं बज्नर यादवनन्दनम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11852)
- **Original**: 34 स द्दर्श ततो व्यास फाल्गुन: काननाभ्रयम्‌ । तमुपेत्य॒महाभागं विनयेनाभ्यवादयत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11853)
- **Original**: 35 ते बन्दमान॑ चरणाववलोक्य मुनिश्चिरम्‌। उबाच वाक्य विच्छाय: कथमद्य त्वमीदृश:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11854)
- **Original**: 36 अवीरजो5नुगमन ब्रह्महत्या कृताथ वा। दृढाशाभड्डदुःखीव भ्रष्टच्छायोअंस साम्प्रतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11855)
- **Original**: 37 सान्तानिकादयो वा ते याचमाना निराकृता: । अगम्यस्त्रीरतिवाँ त्वे बेनासि विगतप्रभ:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11856)
- **Original**: 38 का कपणिकामि इस नवाज विप्रेभ्यो मिष्टमेको5थ वा भवान्‌। कि वा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11857)
- **Original**: 39 खा कस मरी लीला करमनता गोचरत्व॑ गतो्जुन । -_- प्ले निइश्रीक: कथपन्यथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11858)
- **Original**: 40 स्पृश्ो नखाम्भसा बाथ घटवार्युक्षितोषपि वा । केन ते बासि विच्छायो न्यूनेबा युधि निर्जित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11859)
- **Original**: 49 प्रश्नम अंज् 497 बाणोंके समाप्त हो जानेपर घनञ्जय आर्जुनने घनुषकी नॉकसे ही प्रहार करना आरम्भ किया, किन्तु है म॒ने ! ये दस्युगण उन प्रहारोंकी और भी हँसी उड़ाने लगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11860)
- **Original**: हे मुनिश्रेष्ट
- **Translation**: 

---

