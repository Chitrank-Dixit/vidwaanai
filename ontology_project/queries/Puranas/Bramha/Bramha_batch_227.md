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

### Verse 1 (Bramha 0.4521)
- **Original**: लिये अक्षय होता है तथा मनोवाज्छित भोग और मड्भगलमय अवसर प्रास हुआ है। अब तो तुम जो
- **Translation**: 

---

### Verse 2 (Bramha 0.4522)
- **Original**: मोक्ष प्रदान करता है। यहाँ भगवान्‌ श्रीविष्णु और कहो, वहां मुझे करना है; और कुछ नहीं।
- **Translation**: 

---

### Verse 3 (Bramha 0.4523)
- **Original**: शिवके उपाख्यानको जानकर स्नान करनेसे मुक्ति परलोक और धर्मके लिये उत्तम पुत्रके समान
- **Translation**: 

---

### Verse 4 (Bramha 0.4524)
- **Original**: प्राप्त होती है। यह उपाख्यान धन, यश, आयु, कोई सहायक नहीं है। संकटमें पड़े हुए पुरुषके ' आरोग्य और पुण्यकी वृद्धि करनेवाला है। जो लिये स्त्रीके समान दूसरी कोई ओषधि नहीं है।
- **Translation**: 

---

### Verse 5 (Bramha 0.4525)
- **Original**: लोग इस तीर्थंके माहात्म्यको सुनते और पढ़ते हैं, नि:श्रेयस-पदकी प्राप्ति तथा पापसे मुक्ति करानेके
- **Translation**: 

---

### Verse 6 (Bramha 0.4526)
- **Original**: वे पुण्यके भागी होते हैं। उन्हें यहीं-इसी लिये गज्जांके समान कोई नदी नहीं है। धर्म,
- **Translation**: 

---

### Verse 7 (Bramha 0.4527)
- **Original**: जीवनमें भगवान्‌ विष्णु और शिवकी स्मृति प्रात अर्थ, काम और मोक्षकी सिद्धि तथा पापसे
- **Translation**: 

---

### Verse 8 (Bramha 0.4528)
- **Original**: होती है, जो समस्त पापराशिका संहार करनेवाली छुटकारा पानेके लिये श्रीशिव और श्रीविष्णुके
- **Translation**: 

---

### Verse 9 (Bramha 0.4529)
- **Original**: है तथा जिसके लिये जितेन्द्रिय एवं मनोजयी मुनि एकत्व-ज्ञानसे बढ़कर दूसरा कोई साधन नहीं
- **Translation**: 

---

### Verse 10 (Bramha 0.4530)
- **Original**: भी प्रार्थना करते रहते हैं। है। पतिक्रते! तुम्हारी बुद्धिसे तथा श्रोशिव,
- **Translation**: 

---

### Verse 11 (Bramha 0.4531)
- **Original**: इन्द्रके इस कथनका अनुमोदन करते हुए श्रोविष्णु और गद्जाके प्रसादसे मुझे यह सब
- **Translation**: 

---

### Verse 12 (Bramha 0.4532)
- **Original**: देवताओं और ऋषियोंने कहा, 'ऐसा हो होगा।' #>+“जसेंसे904++
- **Translation**: 

---

### Verse 13 (Bramha 0.4533)
- **Original**: * आपस्तम्बतीर्थ, शुक्लतीर्थ और श्रीविष्णुतीर्थकी मद्ठिमा « 221 आपस्तम्बतीर्थ, शुक्लतीर्थ और श्रीविष्णुतीर्थकी महिमा बह्माजी कहते हैं-- आपस्तम्बतीर्थ तीनों लोकोंमें
- **Translation**: 

---

### Verse 14 (Bramha 0.4534)
- **Original**: एक ही है। उसे ही परक्रह्म कहते हैं। गुण और विख्यात है। वह स्मरण करनेमात्रसे समस्त
- **Translation**: 

---

### Verse 15 (Bramha 0.4535)
- **Original**: कर्मके भेदसे एककी ही अनेक रूपोंसे अभिव्यक्ति पापराशिका विध्वंस करनेमें समर्थ है। आपस्तम्ब
- **Translation**: 

---

### Verse 16 (Bramha 0.4536)
- **Original**: होती है। लोकोंका उपकार करनेके लिये एक हो एक मुनि थे। वे परम बुद्धिमान्‌ और महायशस्वी
- **Translation**: 

---

### Verse 17 (Bramha 0.4537)
- **Original**: ब्रह्मके तीन रूप हो जाते हैं। जो इस परमतत्त्वको थे। उनकी पत्नीका नाम अक्षसूत्रा था, वह
- **Translation**: 

---

### Verse 18 (Bramha 0.4538)
- **Original**: जानता है, वही दिद्वान्‌ है; दूसरा नहीं। जो इन पातिब्रत-धर्मका पालन करनेवाली थीं। मुनिके
- **Translation**: 

---

### Verse 19 (Bramha 0.4539)
- **Original**: तीनोंमें भेद बतलाता है, उसे लिम्नभेदी कहते हैं। एक पुत्र थे, जो “कर्की ' नामसे विख्यात थे। वे
- **Translation**: 

---

### Verse 20 (Bramha 0.4540)
- **Original**: उसके लिये कोई प्रायश्चित्त नहीं है।* तीनों बड़े विद्वान्‌ और तत्ववेत्ता थे। एक दिन उनके
- **Translation**: 

---

