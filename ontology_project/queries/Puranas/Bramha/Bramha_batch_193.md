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

### Verse 1 (Bramha 0.3841)
- **Original**: विवाहके पश्चात्‌ महाराजने बड़े हर्षके साथ थे, उनका विचार जानकर बोले-“महाराज!
- **Translation**: 

---

### Verse 2 (Bramha 0.3842)
- **Original**: बहुत-सी गौएँ, सुवर्ण और अश्व आदि सामग्री पूर्वदेशमें विजय नामके एक राजा हैं। उनके पास
- **Translation**: 

---

### Verse 3 (Bramha 0.3843)
- **Original**: दहेजमें देकर कनन्‍्याकों विदा किया। साथ ही घोड़े, हाथी और रत्नोंकी गिनती नहीं है। महाराज
- **Translation**: 

---

### Verse 4 (Bramha 0.3844)
- **Original**: अपने अमात्योंकों भी भेजा। बूढ़े मन्त्री आदि विजयके आठ पुत्र हैं, जो बड़े धनुर्धर हैं। उनकी
- **Translation**: 

---

### Verse 5 (Bramha 0.3845)
- **Original**: सचिवोंने प्रतिष्ठाममें आकर महाराज शूरसेनको बहिन भोगवत्ती साक्षात्‌ लक्ष्मीके समान है। रजन्‌! [उनकी पुत्रवधू समर्पित कर दी। राजा विजयने जो वह आपके पुन्नके लिये सुयोग्य पत्नी होगी।'
- **Translation**: 

---

### Verse 6 (Bramha 0.3846)
- **Original**: विनयपूर्ण बचन कहे थे, उनको भी सुनाया और यूढे अमात्यको बात सुनकर राजाने उत्तर
- **Translation**: 

---

### Verse 7 (Bramha 0.3847)
- **Original**: उनकी दो हुई दहेजकी सामग्री--विचित्र आभूषण, दिया--' राजा विजयकी वह कन्या मेरे पुत्रके
- **Translation**: 

---

### Verse 8 (Bramha 0.3848)
- **Original**: दासियाँ तथा वस्त्र आदि निवेदन किये। इन सब
- **Translation**: 

---

### Verse 9 (Bramha 0.3849)
- **Original**: * भागतीर्धंकी महिप्ता * 189 ..7छछऋऋऋऋऋऋछछऋऋऋनऋगऋऋनचन्च्न्य्ःः््स्ब-- 77777 >«ऋछ777 3 छछ 35377: कार्योंका सम्पादन करके वे लोग कृतकृत्य हो
- **Translation**: 

---

### Verse 10 (Bramha 0.3850)
- **Original**: जोड़कर कहा-“मैं धन्य और अनुगृहीत हूँ, गये। राजकुमारी भोगवतीके साथ जो विजयके
- **Translation**: 

---

### Verse 11 (Bramha 0.3851)
- **Original**: जिसके पति देवता हैं। पति ही स्त्रीकी गति है।' अमात्य पधारे थे, उनका महाराज शूरसेनने बड़े
- **Translation**: 

---

### Verse 12 (Bramha 0.3852)
- **Original**: यह सुनकर नागको बड़ी प्रसन्नता हुई। उसने सम्मानके साथ स्वागत-सत्कार किया। जिसे
- **Translation**: 

---

### Verse 13 (Bramha 0.3853)
- **Original**: हँसकर कहा--'सुन्दरो ! मैं तुम्हारी भक्तिसे सुनकर राजा बिजयको प्रसन्नता हो, ऐसा बर्ताव
- **Translation**: 

---

### Verse 14 (Bramha 0.3854)
- **Original**: संतुष्ट हूँ। बोलो, तुम्हें क्या अभीष्ट बरदान दूँ ? करके सबको बिदा किया। राजा विजयकी कन्या
- **Translation**: 

---

### Verse 15 (Bramha 0.3855)
- **Original**: तुम्हारे अनुग्रहसे मेरी सम्पूर्ण स्मरणशक्ति जाग रूपबती थीं। वह सुन्दरी सदा अपने सास-
- **Translation**: 

---

### Verse 16 (Bramha 0.3856)
- **Original**: उठी है। मुझे पिनाकधारी देवाधिदेव भगवान्‌ ससुरकी सेवामें संलग्न रहती थी। भोगवर्ीका
- **Translation**: 

---

### Verse 17 (Bramha 0.3857)
- **Original**: शंकरने शाप दिया है। शेषनागका पुत्र महाबलबान्‌ पति अत्यन्त भीषण महानाग रत्लोंसे सुशोभित
- **Translation**: 

---

### Verse 18 (Bramha 0.3858)
- **Original**: नाग जो भगवान्‌ शंकरके हाथका कड्कभूण बना एकान्त गृहमें सुगन्धित पुष्पोंसे बिछी हुईं सुखद
- **Translation**: 

---

### Verse 19 (Bramha 0.3859)
- **Original**: रहता है, वहीं मैं तुम्हारा पति हूँ और तुम भी शय्यापर आराम करता था। उसने अपने माता-
- **Translation**: 

---

### Verse 20 (Bramha 0.3860)
- **Original**: वही पूर्वजन्मकी मेरी पत्नी भोगवती हो। एक पितासे बार-बार कहा, 'मेरी पत्नी राजकुमारी मेरे
- **Translation**: 

---

