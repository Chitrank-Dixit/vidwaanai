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

### Verse 1 (Agni Puran 0.6321)
- **Original**: ।), दो जगण (।5।) एवं एक
- **Translation**: 

---

### Verse 2 (Agni Puran 0.6322)
- **Original**: गुरु हों, वह 'भद्गविराट्‌* नामक छन्द है। जिसके जगण हो, वह “द्वुतमध्या* नामक छन्द होता है।
- **Translation**: 

---

### Verse 3 (Agni Puran 0.6323)
- **Original**: प्रथम पादमें सगण, जगण, सगण और एक गुरु (यहाँ भी प्रथम पादके समान तृतीय पाद और
- **Translation**: 

---

### Verse 4 (Agni Puran 0.6324)
- **Original**: तथा द्वितीय पादमें भगण, रगण, नगण और दो द्वितीय पादके समान चतुर्थ पाद जानना चाहिये।
- **Translation**: 

---

### Verse 5 (Agni Puran 0.6325)
- **Original**: गुरु हों, उसका नाम “केतुमती « है। जिसके पहले यही बात आगेके छन्‍्दोंमें भी स्मरण रखनेयोग्य
- **Translation**: 

---

### Verse 6 (Agni Puran 0.6326)
- **Original**: चरणमें दो तगण, एक जगण और दो यही बात आगेके डन्दोंमें भी स्मरण रखनेयोग्य
- **Translation**: 

---

### Verse 7 (Agni Puran 0.6327)
- **Original**: चरणमें दो तगण, एक जगण और दो गुरु हों तथा 1. रासा कामकरेणुका मृगायतनेत्रा, हृदय हरति पयोघरावनप्रा। इधमठिशयसुभगा, ललिताडी फपुष्टविषुष्टमनोहरं मन्मथकेलिनिकेतनमेतत्‌
- **Translation**: 

---

### Verse 8 (Agni Puran 0.6328)
- **Original**: 5. यप्तपि शीघ्रगति्मृदुगामी बहुधनयानपि दुःखमुपैति। वातिशयत्वरिता न च मूद्टी नृपतिगति: कविता द्ुतमध्या
- **Translation**: 

---

### Verse 9 (Agni Puran 0.6329)
- **Original**: 6. तब मुझ नराधिपसेनां बेशवर्तीं सहते समरेषु।प्रलयोगिमिवाभिमुखों तां कः सकलशक्षितिभून्निवहेषु
- **Translation**: 

---

### Verse 10 (Agni Puran 0.6330)
- **Original**: 7. यत्पादतले चकास्ति चक्र हस्ते या कुलिश सरोरुहँ या। राजा जगदेकचक्रव्ती स्थाच्छ॑ भद्गविराट्‌ समश्ुुतेउसी
- **Translation**: 

---

### Verse 11 (Agni Puran 0.6331)
- **Original**: 8. इतभूरिभूमिषतिचिहां युद्धसहल्ललब्धजयलक्ष्मीम्‌। सहते न कोऊपि बसुधायां केतुमतीं नरेद्र तब सेनाम्‌
- **Translation**: 

---

### Verse 12 (Agni Puran 0.6332)
- **Original**: दूसरे चरणमें जगण, तंगण, जगण एवं दो गुरु हों,
- **Translation**: 

---

### Verse 13 (Agni Puran 0.6333)
- **Original**: तथा दूसरेमें एक नगणं, दो जगण, एक रगण और उसे “आख्यानिकी”" कहते हैं। इसके विपरीत यदि
- **Translation**: 

---

### Verse 14 (Agni Puran 0.6334)
- **Original**: एक गुरु हो, उसका नाम ' पुष्पिताग्रा * है। जिसके प्रथम चरणमें जगण, तगण, जगण एवं दो गुरु हों
- **Translation**: 

---

### Verse 15 (Agni Puran 0.6335)
- **Original**: पहले चरणमें रगण, जंगण, रगण, जगण हो तथा और द्वितीय चरणमें दो तंगण, एक जगण तथा दो
- **Translation**: 

---

### Verse 16 (Agni Puran 0.6336)
- **Original**: दूसरेमें जगण, रगण, जगण, रगण और एक गुरु गुरु हों तो उसकी “विपरीताख्यानकी”' संज्ञा
- **Translation**: 

---

### Verse 17 (Agni Puran 0.6337)
- **Original**: हो उसे 'यवमती" कहते हैं। जिसके प्रथम और होती है। जिसके पहले पादमें तीन सगण, एक
- **Translation**: 

---

### Verse 18 (Agni Puran 0.6338)
- **Original**: तृतीय चरणोॉमें अद्टाईस लघु और अन्तमें एक गुरु लघु और एक गुरु हों तथा दूसरेमें नगण, भगण,
- **Translation**: 

---

### Verse 19 (Agni Puran 0.6339)
- **Original**: हो तथा दूसरे एवं चौथे चरणोंमें तीस लघु एवं भगण एवं रगण मौजूद हों, उस छन्दका नाम
- **Translation**: 

---

### Verse 20 (Agni Puran 0.6340)
- **Original**: एक गुरु हों तो उसका नाम 'शिखा" होता है। हरिणप्लुता" है। जिसके प्रथम चरणमें दो नगण,
- **Translation**: 

---

