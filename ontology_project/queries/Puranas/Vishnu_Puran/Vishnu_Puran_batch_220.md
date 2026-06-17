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

### Verse 1 (Vishnu Puran 0.4381)
- **Original**: किन्तु आप जो इस प्रकार भाषण कर रहे हैं उससे मुझे निश्चय होता है कि ये ही भ्रगवान्‌ कपिछटेव मेरे हितकी कामनासे यहाँ आपके रूपमें प्रकट हो गये हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4382)
- **Original**: अतः: हे ट्विज ! हमारा जो परम थ्य हो बह आप मुझ विनीतसे कहिये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4383)
- **Original**: हे प्रधो ! आप सम्पूर्ण विजान-तरंगोंके मानो समुद्र ही हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4384)
- **Original**: ब्राह्मण बोले--हे यजन्‌ ! तुम श्रेय पूछना चाहते हो या परमार्थ ? क्योंकि हे भूफ्ते ! श्रेय तो सब अपारमार्थिक ही हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4385)
- **Original**: हे नृप ! जो पुरुष देवताओंको आराधना करके घन, सम्पत्ति, पुत्र और राज्यादिको इच्छा करता है उसके लिये तो के ही परम श्रेय है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4386)
- **Original**: जिसका फल स्वर्गलोकक्े प्राप्ति है वह यज्ञात्मक कर्म भी श्रेय है; किन्तु प्रधान श्रेय तो उसके फलकी इच्छा न करनेपें हो है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4387)
- **Original**: अत: हे राजन्‌ ! योगयुक्त पुरुषोंक्ो प्रकृति आदिसे अतीत डस्र आत्माका ही ध्यान करना चाहिये, क्योंकि उस परमात्माका संयोगरूप श्रेय ही वास्तविक श्रेय है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4388)
- **Original**: इस प्रकार श्रेय तो सैकडॉ-हजारों प्रकारके अनेकों किंतु ये सब परमार्थ नहीं हैं। अब जो परमार्थ है सो सुनो--
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4389)
- **Original**: यदि घन ही परसमार्थ है तो धर्मके लिये उसका स्थाग क्‍यों किया जाता है ? तथा इच्छित भोगोंकी प्राप्तिके लिये उसका व्यय क्यों किया जाता है ? [अतः वह परमार्थ नहीं है]
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4390)
- **Original**: हे नरेश्वर ! यदि पुत्रको परमसार्थ कहा जाय तो यह तो अन्य (अपने पिता) का परमार्थभूत है, तथा उसका पिता भी दूसरेका पुत्र होनेके कारण तस (अपने पिता) का परमार्थ होगा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4391)
- **Original**: अतः इस चराचर जगत पिताका कार्यरूप पुत्र भो परमार्थ नहीं है। क्योंकि फिर तो सभी कारणोंके कार्य परमार्थ हो जायेंगे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4392)
- **Original**: यदि संसारमें राज्यादिकी प्राप्तिकों परमार्थ कहा जाय तो ये कभो रहते हैं और कभी नहीं रहते। मतः परमार्थ 'नी आगमापायी हो जायगा। [ इसलिल्ये राज्यादि भी परमार्थ नहीं हो सकते ]
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4393)
- **Original**: यदि ऋक्‌, यजू: और सामरूप वेदजयीसे सम्पन्न होनेबाले यज्ञकर्मको परमार्थ मानते हो
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4394)
- **Original**: 156 श्रीविष्णुप्राणं [ अ 14 यक्तु निष्पाद्यते कार्य मृदा कारणभूतया
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4395)
- **Original**: तत्कारणानुगमनाज्ज्ञायते नृष मृण्मयम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4396)
- **Original**: 22 एबं विनाशिभिर्द् व्यू: समिदाज्यकुशादिभिः । निष्पाछते क्रिया या तु सा भवित्री विनाशिनी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4397)
- **Original**: 23 अनाशी परमार्थञ्र॒प्राजैरभ्युपगम्यते । तत्तु नाशि न सन्‍्देहों नाशिद्रव्योपपादितम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4398)
- **Original**: 24 तदेवाफलद कर्म परमार्थों मतस्तव। मुक्तिसाधनभूतत्वात्परमार्थो न साधनम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4399)
- **Original**: 25 ध्यान॑ चैवात्मनो भूप परमार्थार्थशब्दितम्‌ । प्रेदकारि परेभ्यस्तु परमार्थों न भेदबान
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4400)
- **Original**: 26 परमात्मात्मनोयोंग: परमार्थ इतीष्यते मिथ्यैतदन्यदद्ठव्यं हि नैति तदद्॒ब्यतां यतः
- **Translation**: 

---

