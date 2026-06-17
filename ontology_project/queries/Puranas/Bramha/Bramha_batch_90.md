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

### Verse 1 (Bramha 0.1781)
- **Original**: ताभिमाँ सर्वतो रक्ष पिता पुत्रमिवौरसम्‌
- **Translation**: 

---

### Verse 2 (Bramha 0.1782)
- **Original**: रक्ष मां रक्षणोयो5ह॑ तवातथ नमोउस्तु _ते। भछानुकम्पी भगवान्‌ भक्तक्षाह सदा त्वयि
- **Translation**: 

---

### Verse 3 (Bramha 0.1783)
- **Original**: यः सहस्राण्वनेकानि पुंसामावृत्य दुर्दु्षाम्‌। तिष्ठत्येक: समुद्रात्ते स मे गोह्ास्तु नित्यशः
- **Translation**: 

---

### Verse 4 (Bramha 0.1784)
- **Original**: य॑ बिनिद्रा जितश्रासा: सत्वस्था: समदर्शिन:। ज्योति: पश्यन्ति युज्ञानास्तस्मै योगात्मने नमः #
- **Translation**: 

---

### Verse 5 (Bramha 0.1785)
- **Original**: सम्भक्ष्य सर्वभूतानि युगान्ते समुपस्थिते । यः शेते जलमध्यस्थस्त प्रपच्चे5म्बुशायिनम्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.1786)
- **Original**: प्रबिश्य बदन राषहोर्य: सोम॑ पिबते तिशि। ग्रसत्यक॑च॒स्वर्भानुर्भूत्वा सोमाग्रिरिव च
- **Translation**: 

---

### Verse 7 (Bramha 0.1787)
- **Original**: अज्जुष्टमात्रा: पुरुषा देहस्था; सर्वदेहिनाम्‌ । रक्षन्तु ते व मां नित्य नित्यं चाप्याययन्तु सास
- **Translation**: 

---

### Verse 8 (Bramha 0.1788)
- **Original**: येनाष्युत्पादिता गर्भा अपो भागगताक्ष ये । तेषां स्थाहा स्वथा चैंव आप्नुवन्ति स्वदन्ति च
- **Translation**: 

---

### Verse 9 (Bramha 0.1789)
- **Original**: ये न रोदन्ति देहस्था: प्राणिनों रोदयन्ति च। हर्षयन्ति न दृष्यन्ति नमस्तेध्यस्तु निल्यशड
- **Translation**: 

---

### Verse 10 (Bramha 0.1790)
- **Original**: ये सपुद्रे नदोदुर्गे पर्वठेषु गुहासु च। वृक्षमलेषु गोहेषु कान्तारगहनेषु च
- **Translation**: 

---

### Verse 11 (Bramha 0.1791)
- **Original**: *एकाग्रकक्षेत्र तथा पुरुषोत्तमक्षेत्रकी महिमा « <9 हैं। इसीलिये आपको पृथक्‌ निमन्त्रित नहीं किया
- **Translation**: 

---

### Verse 12 (Bramha 0.1792)
- **Original**: सम्पूर्ण देबताओंमें भगवान्‌ शिव श्रेष्ठ हैं, उसी गया। देव! भाँति-भाँतिकी दक्षिणावाले यज्ञोंद्वारा
- **Translation**: 

---

### Verse 13 (Bramha 0.1793)
- **Original**: प्रकार सब स्तोत्रोंमें यह दक्षनिर्मित स्तोत्र श्रेष्ठ है। आपका ही यजन किया जाता है। आप ही सबके
- **Translation**: 

---

### Verse 14 (Bramha 0.1794)
- **Original**: जो लोग यश, स्वर्ग, देवताओंका ऐश्वर्य, धन, कर्ता-धर्ता हैं, इसलिये आपको मैंने निमन्त्रित, विजय और ब्िद्या आदिकी अभिलाषा रखते हैं, नहीं किया। अथवा देव! आपकी सूक्ष्म-दुर्बोध
- **Translation**: 

---

### Verse 15 (Bramha 0.1795)
- **Original**: उन्हें यत्रपूर्वकत भक्तिके साथ इस स्तोत्रद्वारा भगवान्‌ मायासे मैं मोहित था। इसी कारण आपको
- **Translation**: 

---

### Verse 16 (Bramha 0.1796)
- **Original**: शिवकी स्तुति करनी चाहिये। रोगी, दुःखी, दीन, निमनत्रण नहीं दिया। देवेश्वर! मुझपर प्रसन्न
- **Translation**: 

---

### Verse 17 (Bramha 0.1797)
- **Original**: भय आदिसे ग्रस्त तथा राज-काजमें नियुक्त मनुष्य होइये। आप ही मुझे शरण देनेवाले हैं। आप ही
- **Translation**: 

---

### Verse 18 (Bramha 0.1798)
- **Original**: इस स्तोत्रके प्रभावसे महान्‌ भयसे मुक्त हो जाता मेरी गति और प्रतिष्ठा हैं, दूसरा कोई नहीं है।
- **Translation**: 

---

### Verse 19 (Bramha 0.1799)
- **Original**: है तथा भगवान्‌ शिवसे इस लोकमें सुख पाकर ऐसा मेरा दृढ़ विश्वास है।" उसी शरीरसे गणोंका स्वामी बन जाता है। यक्ष, इस प्रकार महादेवजीकी स्तुति करके प्रजापति
- **Translation**: 

---

### Verse 20 (Bramha 0.1800)
- **Original**: पिशाच, नाग और विनायक उस मनुष्यके घरमें दक्ष चुप हो गये। तब भगवान्‌ शिवने कहा--“ उत्तम
- **Translation**: 

---

