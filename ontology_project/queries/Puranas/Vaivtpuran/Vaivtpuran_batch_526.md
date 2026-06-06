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

### Verse 1 (Vaivtpuran 32.7657)
- **Original**: लगा है, लोहेके आभूषणोंसे भूषित हूँ, अड॒हुलके निकट अक्षयवटके नीचे भृगुवंशी परशुराम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7658)
- **Original**: फूलोंकी माला पहने हूँ और गधेपर चढ़कर हँस भाइयोंसहित पधारे हुए हैं। वे इक्कीस बार रहा हूँ तथा बुझे हुए अंगारोंकी राशिसे क्रौड़ा पृथ्वीको राजाओंसे शून्य करेंगे। अत: आप वहाँ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7659)
- **Original**: कर रहा हूँ। पतित्रते! पृथ्वीपर अड॒हुलके पुष्प चलिये अथवा भाई-बन्धुओंके साथ युद्ध कौजिये।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7660)
- **Original**: बिखरे हुए हैं और वह राखसे आच्छादित हो इतना कहकर परशुरामका दूत उनके पास लौट
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7661)
- **Original**: गयी है। आकाश चन्द्रमा और सूर्यसे रहित होकर गया। इधर राजा कवच धारण करके रण-दयात्राके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7662)
- **Original**: संध्याकालीन लालिमासे व्याप्त हो गया है। मैंने लिये उद्यत हुआ। तब महारानी मनोरमाने अपने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7663)
- **Original**: एक विधवा स्त्रीको देखा, जो लाल वस्त्र पहने प्राणपतिको युद्धमें जानेके लिये उद्यत देख उसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7664)
- **Original**: थी, केश खुले थे, नाक कट गयी थी और वह रोक दिया और अपने पास ही बैठा लिया। मुने!
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7665)
- **Original**: अट्टहास करती हुई नाच रही थी। महारानी! मैंने मनोरमाकों देखकर राजाके नेत्र और मुख
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7666)
- **Original**: एक चिता देखी, जिसपर बाण बिछे थे और प्रसन्नतासे खिल उठे। फिर तो उसने सभाके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7667)
- **Original**: वह अग्रिसे रहित एवं भस्मसे संयुक्त थी। फिर बीच रानीसे अपने मनकी बात कही। राखकी वर्षा, रक्तकी वर्षा और अंगारोंकी वर्षा कार्तवीर्यार्जुन कहने लगा-- प्रिये! जमदग्रिके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7668)
- **Original**: होते हुए देखा। पृथ्वी पके हुए ताड़के फलोंसे महान्‌ पराक्रमी पुत्र परशुराम भाइयोंके साथ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7669)
- **Original**: आच्छादित और हहड्डियोंसे संयुक्त थी। फिर नर्मदा-तटपर ठहरे हुए हैं। वे मुझे युद्धेके लिये
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7670)
- **Original**: खोपड़ियोंकी ढेरी दीख पड़ी, जो कटे हुए बालों ललकार रहे हैं। उन्हें शंकरजीसे शस्त्र और
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7671)
- **Original**: और नखोंसे युक्त थी। फिर रातके समय नमकका श्रीहरिका मन्त्र तथा कवच प्राप्त हो गया है; पहाड़, कौड़ियोंकी ढेरी और धूल तथा तेलकी अतः वे इक्कीस बार भूमिको भूपालोंसे होन कर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7672)
- **Original**: कन्दरा दृष्टिगोचर हुई। फिर फूलोंसे लदे हुए
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7673)
- **Original**: 366 * संक्षिप्त ब्रह्मवैवर्तपुराण + 00400444 04 40 8
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7674)
- **Original**: । । ।।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7675)
- **Original**: ।2)]]]]] रत अशोक और करबीरके वृक्ष दीख पड़े। वहीं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7676)
- **Original**: नखोंकी खरोंच लगी है; रातमें मैंने ऐसा भी ताड़के वृक्ष भी थे, जिनमें फल लगे थे और
- **Translation**: 

---

