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

### Verse 1 (Vaivtpuran 13.10782)
- **Original**: क हक कक ऋ कक कलावतीकी बात सुनकर विधाता विस्मित
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10783)
- **Original**: भी अयोनिजा, पूर्व-जन्मकी बातोंको याद रखनेवाली हो मन-ही-मन भय मानते हुए अमृतके समान
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10784)
- **Original**: महासाध्वी, सुन्दरी एवं कमलाकी कला थी। मधुर एवं हितकर वचन बोले। कान्यकुब्ज देशमें महापराक्रमी नृपश्रेष्ठ भनन्दन ब्रह्माजीने कहा--बेटी ! मैं तुम्हारे स्वामीको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10785)
- **Original**: राज्य करते थे। उन्होंने यज्ञके अन्तमें यज्ञकुण्डसे तुम्हारे बिना ही मुक्ति नहीं दूँगा। पतिब्रते! तुम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10786)
- **Original**: प्रकट हुई दूध पीती नंगी बालिकाके रूपमें उसे अपने पतिके साथ कुछ वर्षोतक स्वर्गमें रहकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10787)
- **Original**: पाया था। वह सुन्दरी बालिका उस कुण्डसे सुख भोगो। फिर तुम दोनोंका भारतवर्षमें जन्म
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10788)
- **Original**: हँसती हुई निकली थी। उसकी अजद्भ-कान्ति होगा। वहाँ जब साक्षात्‌ सत्ती राधिका तुम्हारी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10789)
- **Original**: तपाये हुए सुवर्णक समान थी। वह तेजसे पुत्री होंगी तब तुम दोनों जीवन्मुक्त हो जाओगे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10790)
- **Original**: उद्धांसित हो रही थी। राजेन्द्र भनन्दनने उसे और श्रीराधाके साथ ही गोलोकमें पधारोगे।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10791)
- **Original**: गोदमें लेकर अपनी प्यारी रानी मालावतीको नृपश्रेष्ठ! तुम कुछ कालतक अपनी स्त्रीके साथ
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10792)
- **Original**: प्रसन्नतापूर्वक दे दिया। मालावतीके हर्षकी सीमा स्वर्गीय सुखका उपभोग करो। यह स्त्री साध्वी न रही। वह उस बालिकाकों अपना स्तन एवं सत्त्वगुणसे युक्त है। तुम मुझे शाप न देना;
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10793)
- **Original**: पिलाकर पालने लगी। उसके अन्नप्राशन और क्योंकि श्रीकृष्णके चरणारविन्दोंमें चित्त लगाये
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10794)
- **Original**: नामकरणके दिन शुभ बेलामें जब राजा सत्पुरुषोंके रखनेवाले जीवन्मुक्त संत समदर्शी होते हैं। उनके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10795)
- **Original**: बीच बैठे हुए थे, आकाशवाणी हुई--“नरेश्वर ! मनमें श्रीहरिके दुर्लभ दास्यभावकों पानेकी इच्छा [इस कन्याका नाम कलावती रखो।' यह सुनकर रहती है। वे निर्वाण नहीं चाहते। राजाने वही नाम रख दिया। उन्होंने ब्राह्मणों, ऐसा कहकर उन दोनोंकों वर दे विधाता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10796)
- **Original**: याचकों और वन्दीजनोंको प्रचुर धन दान किया। उनके सामने खड़े रहे। वे दोनों उन्हें प्रणाम करके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10797)
- **Original**: सबको भोजन कराया और बड़ा भारी उत्सव स्वर्गकी ओर चल दिये। फिर ब्रह्माजी भी अपने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10798)
- **Original**: मनाया। समयानुसार उस रूपवती कन्याने युवावस्थामें धामको चले गये। तदनन्तर वे दोनों दम्पति
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10799)
- **Original**: प्रवेश किया। सोलह वर्षकी अवस्थामें वह समयानुसार स्वर्गीय भोगोंका उपभोग करके भारतवर्षमें
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10800)
- **Original**: अत्यन्त सुन्दरी दिखायी देने लगी। वह राजकन्या आये, जो परम पुण्यदायक तथा दिव्य स्थान है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10801)
- **Original**: मुनियोंके मनको भी मोह लेनेमें समर्थ थी। ब्रह्मा आदि देवता भी वहाँ जन्म लेनेकी इच्छा [मनोहर चम्पाके समान उसकी अड्भकान्ति थी करते हैं। सुचन्द्रने गोकुलमें जन्म लिया और वहाँ
- **Translation**: 

---

