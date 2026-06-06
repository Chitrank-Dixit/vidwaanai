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

### Verse 1 (Sama Ved 0.1121)
- **Original**: इन्द्रदेव अन्न, सोम आदि से पूर्व, गौओं को देने में समर्थ दृढ़ रथ को भलीप्रकार जानते हैं और उसी पर आसीन होते हैं। अतः है इद्धदेव ! आप अपने घोड़ों को रथ में जोड़ें ( ताकि सभी वाज्छित पदार्थ हम तक पहुँचा सकें)
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1122)
- **Original**: 425. अग्नि त॑ मन्‍ये यो वसुरस्तं य॑ यन्ति धेनवः । अस्तमर्वन्त आशवोःसतं नित्यासों वाजिन इषं स्तोतृभ्य आ भर
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1123)
- **Original**: जो अग्नि (लेटेण्ड हीट) मेघों में आवास बनाकर रहती है, यज्ञस्थल में स्थित जिस अग्नि की ओर गौएँ जाती हैं, जिस ओर तीत्र गतिशील घोड़े गमन करते हैं, जिसकी ओर ह॒विष्यान्‍्नधारी यजमान जाते हैं, ऐसे अग्निदेव को मैं अर्चना करता हूँ । याजकों के लिए वे प्रचुर अन्न प्रदान करें
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1124)
- **Original**: 426. न तमंहो न दुरितं देवासो अष्ट मर्त्यम्‌। सजोषसो यमर्यमा मित्रो नयति वरुणो अति द्विष:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1125)
- **Original**: हे देवो ! एकमत होकर विद्यमान रहने वाले, अर्यमा, मित्र और वरुणदेव दुराचारियों का निराकरण करके मनुष्यों को उन्‍्नतति-मार्ग पर अग्रसर करते हैं, वह मानव पाप रहित होकर दुर्गति से दूर रहता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1126)
- **Original**: इति द्वात्रिंश: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1127)
- **Original**: पूर्वार्विके ऐस्द्रपर्दणि चतृथों 5ध्यायः 4.11
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1128)
- **Original**: त्रय्त्रिश: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1129)
- **Original**: 427. परि प्र धन्वेन्द्राय सोम स्वादुर्मित्राय पृष्णे भगाय
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1130)
- **Original**: हे स्वादिष्ट सोमदेव ! आप इन्द्र, मित्र, पूषा और भग देवताओं के लिए प्रवाहित हों । 1
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1131)
- **Original**: 428. पर्यू घु प्र धन्व वाजसातये परि वृत्राणि सक्षणि: । द्विषस्तरध्या ऋणया न ईरसे
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1132)
- **Original**: है सोमदेव ! आप अन्न को प्राप्त करने के लिए भली-भाँति कलश को पूर्ण करके उसी में अवस्थित रहें । शक्ति-सम्पन होकर आप शत्रुओं पर आक्रमण कर दें । हमें ऋणों से विमुक्त करने वाले आप शत्रुओं को परास्त करने के लिए उन पर आक्रमण करने के लिए जाएँ
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1133)
- **Original**: 429. पवस्व सोम महान्त्समुद्र: पिता देवानां विश्वभि धाम
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1134)
- **Original**: हे सोमदेव ! विस्तृत समुद्र के समान पोषण करने बाले आप देवों के सभी आवास स्थलरूपी पात्रों में विद्यमान रहते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1135)
- **Original**: 430. पवस्व सोम महे दक्षायाश्वों न निक्‍तो वाजी धनाय
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1136)
- **Original**: है सोमदेव ! अश्व के समान (प्रयासपूर्यक) स्वच्छ किये गये, शक्तिवर्द्धध आप बल एवं ऐश्वर्य प्रदान करने के लिए पात्रों में भरे रहें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1137)
- **Original**: 4391. इन्दुः पविष्ट चारुर्मदायापामुपस्थे कविर्भगाय
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1138)
- **Original**: श्रेष्ठ ज्ञान-सम्पनन यह सोम सम्पत्तियुक्त हर्ष की प्राप्ति के लिए जल से संयुक्त किया जाता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1139)
- **Original**: 432: अनु हि त्वा स्रुतं सोम मदामसि महे समर्यराज्ये । वाजाँ अभि पवमान प्र गाहसे
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1140)
- **Original**: है सोमदेव ! रस निचोड़ने के बाद हम आपकी विधिपूर्वक अर्चना करते हैं । हे शोधित सोम ! श्रेष्ठ राजा के रक्षण के निमित्त, शक्तिशाली होकर आप विरोधी सेना पर आक्रमण करने के लिए गमन करते हैं
- **Translation**: 

---

