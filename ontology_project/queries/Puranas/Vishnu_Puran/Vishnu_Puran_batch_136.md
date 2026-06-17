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

### Verse 1 (Vishnu Puran 0.2701)
- **Original**: 23 क्रोधा तु जनयायास पिशाचांश्र महाबलान्‌ । गास्तु वै जनयाप्रास सुरभिर्महिषांस्तथा । इरावृक्षऊतावल्लीस्तृणजातीक्ष. सर्वशञ:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2702)
- **Original**: 24 खसा तु बक्षरक्षांसि मुनिरप्सरसस्तथा । अरिष्टा तु महासत्त्वान्‌ गन्धर्वान्समजीजनत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2703)
- **Original**: 25 एते कश्यपदायादाः कीर्तिता: स्थाणुजड़रमा: । तेषां पुत्राश्न पौत्राअ शतझो5थ सहस्नज्व:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2704)
- **Original**: 26 ए मन्वन्तरे सर्गो ब्रह्मन्स्वारोचिषे स्पृत:ः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2705)
- **Original**: 27 बैवस्वते न महति वारुणे वितते कृतौ। जुद्नानस्य ब्रह्मणो वे प्रजासर्ग इहोच्यते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2706)
- **Original**: 28 पूर्व यत्र तु सप्र्षनित्पन्नान्ससमानसान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2707)
- **Original**: पितृत्वे कल्पयामास स्वयमेव पितामहः । गन्धर्वभोगिदेशानां दानवानां क्र सत्तम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2708)
- **Original**: 29 दितिविनष्टपुत्रा वै तोषयामास काइयपम्‌। तथा चाराधितः सम्यक्लाइयपस्तपतां खर:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2709)
- **Original**: 30 वरेणच्छन्दयामास सा च बत्ने ततो वरम्‌। पुत्रमिद्रवधार्थाय.. समर्थममितौजसम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2710)
- **Original**: 39 शुकीसे शुक्र, उल्कूक एवं उद्मूकोंके प्रतिपक्षी काक आदि उत्पन्न हुए तथा श्येनीसे इयेन (बाज), भासीसे भास और गृद्घिकासे गृद्धोंका जन्प हुआ
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2711)
- **Original**: शुचिसे जल्के पक्षिगण और सुप्रीचीसे अश्व, उट्टू और गर्दभोंकी डतात्ति हुई । इस प्रकार यह ताप्राका वँज्ञ कहा जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2712)
- **Original**: विनताके गरुड्ठ और अरुण ये दो पुत्र विख्यात हैं। इनमें पक्षियोंमें श्रेष्ठ सुपर्ण (गरुड़जी) अति भयंकर और सर्पोको खानेवाले हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2713)
- **Original**: हे अद्यन्‌ । सुरसासे सहस्तरो सर्प उत्पन्न हुए जो बड़े ही प्रभावशाली, आकाझमें विचरनेवाले, अनेक विरोबाले और बड़े विशालकाय थे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2714)
- **Original**: और कइूके पुत्र भी महाबल्ले और अमित तेजस्वी अनेक सिरवाले सहस्रों सर्प ही हुए जो गरुडजीके वशवर्ती थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2715)
- **Original**: उनमेंसे शेष, वासुकि, तक्षक शैखश्वेत, महापद्य, कम्बल, अश्वतर, एलापुत्र, नाग, ककोंटक, धनज्जय तथा और भी अनेकों ठग्न विषधर एवं काटनेवाफे सर्प प्रधान हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2716)
- **Original**: क्रोधवशाके पूत्र क्रोधनशगण हैं। वे सभो बड़ी-बड़ी दाढ़ोवाले, भयंकर और कचा माँस खानेबाले जलूचर, स्थऊछबर एवं पक्षिगण हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2717)
- **Original**: महाबली पिदाचॉक्मे भी व्रनेधाने ही जन्म दिया है। सुरभिसे गौ और महिषर आदिकी उत्पत्ति हुई तथा इरासे वृक्ष, लता, बेल और सब प्रकास्के तृण उत्पन हुए है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2718)
- **Original**: खसाने यक्ष और राक्षसॉको, मुनिने अप्सराओक्ा तथा अरिष्टाने अति समर्थ गन्धवॉक्मरे जन्म दिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2719)
- **Original**: ये रूब स्थावर-जंगम कस्यपजीको सनन्‍्तान हुए। इनके और भी सैकड़ों-हजारों पुत्र-पौत्रादि हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2720)
- **Original**: है ब्रह्मम्‌ ! यह स्वारोचिष -मन्जत्तरकी सृष्टिका वर्णन कहा जाता है
- **Translation**: 

---

