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

### Verse 1 (Vaivtpuran 13.12142)
- **Original**: नाभिकमलमें विराजमान ब्रह्माजी जब मधु और नन्दगोपसुतं कान्तमस्मभ्य॑ देहि सुब्रते
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12143)
- **Original**: कैटभसे पीड़ित हुए, तब उन्होंने इसी स्तोत्रसे “उत्तम ब्रतका पालन करनेवाली हे देवि! हे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12144)
- **Original**: मूलप्रकृति ईश्वरीका स्तवन किया। जगदम्ब ! तुम्हीं जगत्‌की सृष्टि, पालन और संहार *3& नमो जय दुर्गायै' करनलेवाली हो; तुम हमें नन्दगोप-नन्दन श्यामसुन्दको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12145)
- **Original**: . ब्रह्मा बोले--दुर्गे! शिवे! अभये! माये! ही प्राणवल्लभ पतिके रूपमें प्रदान करो।' नारायणि! सनातनि! जये! मुझे मड्जल प्रदान इस मन्त्रसे देवेश्वरी दुर्गाकी मूर्ति बनाकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12146)
- **Original**: करो। सर्वमड्नले ! तुम्हें मेरा नमस्कार है। दुर्गाका संकल्प करके मूलमन्त्रसे उनका पूजन करे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12147)
- **Original**: “दकार' दैत्यनाशरूपी अर्थका वाचक कहा गया सामवेदोक्त मूलमन्त्र बीजमन्त्रसहित इस
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12148)
- **Original**: है। “उकार' विप्ननाशरूपी अर्थका बोधक है। प्रकार है-- उसका यह अर्थ वेदसम्मत है। 'रेफ' रोगनाशक 3» श्रीदुर्गायै सर्वविप्नविनाशिन्य नम: ।--
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12149)
- **Original**: अर्थको प्रकट करता है। 'गकार' पापनाशक इसी मन्त्रसे सब गोपकुमारियाँ भक्तिभाव और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12150)
- **Original**: अर्थता वाचक है। और “आकार' भय तथा प्रसन्नताके साथ देवीको फूल, माला, नैवेद्य, धूप,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12151)
- **Original**: शत्रुओंके नाशका प्रतिपादक कहा गया है। जिनके दीप और वस्त्र चढ़ाती थीं। मूँगेकी मालासे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12152)
- **Original**: चिन्तन, स्मरण और कीर्तनसे ये दैत्य आदि निश्चय भक्तिपूर्वक इस मन्त्रका एक सहस्त जप और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12153)
- **Original**: हो नष्ट हो जाते हैं; वे भगवती दुर्गा श्रीहरिकी स्तुति करके वे धरतीपर माथा टेककर देवीकों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12154)
- **Original**: शक्ति कही गयी हैं। यह बात किसी औरने नहीं, प्रणाम करती थीं। उस समय कहती कि 'समस्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12155)
- **Original**: साक्षात्‌ श्रीहरिने ही कही है। दुर्ग! शब्द मड्भअलॉका भी मज्जल करनेवाली और सम्पूर्ण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12156)
- **Original**: विपत्तिका वाचक है और 'आकार' नाशका। जो कामनाओंको देनेवाली शंकरप्रिये देवि शिवे ! तुम्हें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12157)
- **Original**: दुर्ग अर्थात्‌ विपत्तिका नाश करनेवाली हैं; वे देवी नमस्कार है। तुम मुझे मनोवाज्छित वस्तु
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12158)
- **Original**: ही सदा “दुर्गा' कही गयी हैं। ' दुर्ग' शब्द दैत्यराज दो।' यों कह नमस्कार करके दक्षिणा दे सारे [दुर्गगासुरका वाचक है और “आकार' नाश नैवेद्य ब्राह्मणोंको अर्पित करके वे घरकों चली
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12159)
- **Original**: अर्थका बोधक है। पूर्वकालमें देवीने उस जाती थीं। दुर्गमासुरका नाश किया था; इसलिये विद्वानोंने भगवान्‌ श्रीनारायण कहते हैं--मुने!
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12160)
- **Original**: उनका नाम 'दुर्गा' रखा। शिवा शब्दका 'शकार' अब तुम देवीका वह स्तवराज सुनो, जिससे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12161)
- **Original**: कल्याण अर्थका, 'इकार' उत्कृष्ट एवं समूह सब गोपकिशोरियाँ भक्तिपूर्वक पार्वतीजीका
- **Translation**: 

---

