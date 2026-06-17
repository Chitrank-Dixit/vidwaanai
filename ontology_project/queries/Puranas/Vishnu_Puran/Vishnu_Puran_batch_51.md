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

### Verse 1 (Vishnu Puran 0.1001)
- **Original**: फिर श्रेतनस्नरधारी साक्षात्‌ भगवान्‌ घन्वन्तरिजी अमृतसे भय कमप्डल्ठु लिये अकट हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1002)
- **Original**: हे मैत्रेय ! उस समय मुनिगणके सहित समस्त दैत्य और दानबगण स्वस्थ-चित्त होकर अति प्रसन्न हुए
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1003)
- **Original**: उसके पश्चात्‌ विकसित कमलपर विराजमान स्फुटकान्तिमयी श्रीलक्ष्मीदेवी हाथोंमें कमल-पुष्प धारण किये क्षीर-समुद्रसे प्रकट हुईं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1004)
- **Original**: उस समय महर्चिगण अति प्रसन्नतापूर्वक श्रीसूक्तद्वारा उनकी स्तुति करने लगे तथा विश्वायसु आदि गन्धर्वगण उनके सम्मुख गान और शृताची आदि अप्सराएँ नृत्य करने लगों
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1005)
- **Original**: 101-102
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1006)
- **Original**: उन्हें अपने जरूसे स्नान करानेके लिये गज्ना आदि नदियाँ स्वयं उपस्थित हुई और दिग्गजोंने सुवर्ण-कलद्ॉमें भरे हुए उनके निर्मल जलसे सर्वलेक- म्ेधरी श्रीलक्ष्मीदेतीको स्नान कराया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1007)
- **Original**: क्षीर- सागरने मूर्तिमान्‌ होकर उन्हें लिकसित कमल-पुष्पोंकी माला दी तथा विश्वकर्माने उनके अग-प्रत्यंगर्में विविध आभूषण पहनाये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1008)
- **Original**: इस प्रकार दिव्य मात्झ और
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1009)
- **Original**: डे6 त्तया विल्लेकिता देवा हसिविक्ष:स्थलस्थया । लक्ष्प्या मैत्रेय सहसा परा निर्वतिमागता:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1010)
- **Original**: 106 उद्देंग परम जम्मुर्देत्या विष्णुपराइन्मुखा: । त्यक्ता लक्ष्य्या महाभाग विप्रचित्तिपुरोगमा:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1011)
- **Original**: 107 ततस्ते जगृहदैत्या धन्वन्तरिकरस्थितम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1012)
- **Original**: कमण्डलुं महावीर्या यत्नास्तेज्मृतमुत्तमम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1013)
- **Original**: 108 मायबया मोहयित्वा तान्विष्णु: ख्रीरूपसंस्थित: । दानवेभ्यस्तदादाय देवेभ्य: प्रददौ प्रभुः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1014)
- **Original**: 109 ततः पपुः सुरगणाः दक्राद्यास्तत्तदाउमृतम्‌ । उद्यतायुभनिखतिंशा दैत्यास्तांश् समप्ययु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1015)
- **Original**: 110 पीतेउमते क्र बलिभिरदेवैर्दैत्यचपृस्तदा । बध्यमाना दिज्ञो भेजे पातालं च विवेश वै
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1016)
- **Original**: 111 ततो देवा मुद्धा युक्ता: शब्ब॒च्क्रगदाभृतम्‌ । अ्रणिपत्य यथापूर्वमाशासत्तत्त्रिविष्टपम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1017)
- **Original**: 112 ततः प्रसन्नभा: सूर्य: प्रथयो स्वेन वर्त्मना । ज्योतीषि चर यथामार्ग प्रययुर्मुनिसत्तम
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1018)
- **Original**: 113 जज्वालभगवांश्रोच्ैश्नारुदीप्रिर्विभावसु: । धर्म चर सर्वभूतानां तदा मतिरजायत
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1019)
- **Original**: 114 जैल्मेक्य च॒ प्रिया जुट्ठं बधूव द्विजसत्तम । झक्रश्न त्रिदशश्रेष्ठ; पुनः श्रीमानजायत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1020)
- **Original**: 115 सिंहासनगत:ः शक्रस्सम्प्राप्य जिदिव पुनः । देवराज्ये स्थितो देवीं तुष्टावाब्जकरां तत:
- **Translation**: 

---

