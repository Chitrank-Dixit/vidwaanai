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

### Verse 1 (Vishnu Puran 0.9261)
- **Original**: जैसे मूर्ख मनुष्योंकों घृष्टतापूर्ण उक्तियोंसे अच्छे कक्ताकी खाणी भी मस्किन पड़ जाती है बैसे ही सल्िन मेघोंसे के एक प्रकारके त्थालू कीड़े, जो वर्षा-कारूमें उत्पन्न होते हैं, उन्हें उक्रगोप और वोसबहूटी कहते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9262)
- **Original**: क्केरेड ओतिष्णुपुराण ( आः 6 निर्गुणनापि चापेन शक्रस्थ गगने पदम्‌। अवाप्यताविवेकस्थ॒ नृपस्थेव परिग्रहे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9263)
- **Original**: 40 म्रेघपृष्ठे बल्लाकानां रराज विमला ततिः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9264)
- **Original**: दुर्वुते वृत्तचेष्टल कुलीनस्थातिशोभना
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9265)
- **Original**: 41 न बबन्धाम्बरे स्थै्य॑ विद्युदत्यन्तचस्चला । मैत्रीव प्रवरे पुंसि दुर्जनेन प्रयोजिता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9266)
- **Original**: 42 मार्गा बधूवुरस्पष्टास्तृणशष्यच्यावृता: । अर्थान्तरमनुप्राप्ताः प्रजडानामिषोक्तय:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9267)
- **Original**: 43 उन्मत्तशिखिसारड्डे तस्मिन्‍्काले महावने। कृष्णरामौ मुदा युक्तो गोपालैओरतुस्सह
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9268)
- **Original**: 44 क्रचिज्वेभिस्सम॑ रम्ये गेयतानरताबुभो । चेरतु: क्रचिदत्यर्थ शीतवृक्षतलाभ्रितौ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9269)
- **Original**: 45 क्रचित्कदम्बस्रक्चित्रो . मयूरस््नग्विराजितो । बिलिपौ क्चिदासातां विविधैर्गिरिधातुभि:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9270)
- **Original**: 46 पर्णशय्यासु संसुप्तो क्रलिन्निद्रान्तरैषिणों। क्रचिद्वर्जति जीमूते हाह्काररवाकुलों
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9271)
- **Original**: 47 गायतामन्यगोपानां प्रशंंसापरमौ क्लचित्‌। मयूरकेकानुगता गोपनबेणुप्रवादकौ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9272)
- **Original**: 48 डति नानाविधैभविरुत्तमप्रीतिसंयुतौ । क्रीडन्तो तो बने तस्ििंश्रेरतुस्तुष्टमानसों
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9273)
- **Original**: 49 बिकाले च् सम॑ गोभिगोंपवृन्दसमन्वितौ । विहृत्याथ यथायोगं ब्रजमेत्य महाबल्लौं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9274)
- **Original**: 50 गोपैस्समानैस्सहिताौ. क्रीडन्तान्मराबिज । एवं ताबूघतुस्तत्र रामकृष्णौ महाद्युती
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9275)
- **Original**: 51 आच्छादित रहनेके कारण निर्मछ चन्द्रमा थी शोभाहीन हो गया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9276)
- **Original**: जिस प्रकार विवेकहीन राजाके संगमें गुणहीन मनुष्य भो प्रतिष्ठा प्राप्त कर छेता है उसी प्रकार आकाश- मष्डलमें गुणरहित इन्द्र-धनुष स्थित हो गया।
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9277)
- **Original**: दुराचारी पुरुषमें कुलीन पुरुषकी निष्कपट शुभ चेश्टके समान मेघमण्डलमें बगुलोंकी निर्मल पंक्ति सुशोभित होने लगी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9278)
- **Original**: श्रेष्ठ पुरुषके साथ दुर्जनक्ती मित्रताके समान अत्पत्त चञ्नछा विद्युत्‌ आकादामें स्थिर न रह सकी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9279)
- **Original**: महासूर्ख सनुष्योंकी अन्यार्थिका उक्तियोँके समान मार्ग तण और दूबसमूहसे आयश्नदित होकर अस्पष्ट हो गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9280)
- **Original**: उस समय उच्मत मयूर और चातकगणसे सुशोभित महावनमें कृष्ण और राम प्रसन्नतापूर्वक गोपकुमारोंके साथ बिचरने लगे
- **Translation**: 

---

