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

### Verse 1 (Agni Puran 0.2121)
- **Original**: स्थापना करके, गुरु सूर्य-सम्बन्धी मन्त्र बोलते हुए निर्माण और स्नान आदि कार्यका सम्पादन
- **Translation**: 

---

### Verse 2 (Agni Puran 0.2122)
- **Original**: शक्त्यन्त सूर्यका विधिवत्‌ स्थापन करे
- **Translation**: 

---

### Verse 3 (Agni Puran 0.2123)
- **Original**: करके, पूर्वोक्त विधिसे विद्या तथा साड् सूर्यदेवका
- **Translation**: 

---

### Verse 4 (Agni Puran 0.2124)
- **Original**: श्रीसूर्यदेवका स्वाम्यन्त अथवा पादान्त नाम आसन-शगय्यामें न्यास करके त्रितत््वका, ईश्वरका
- **Translation**: 

---

### Verse 5 (Agni Puran 0.2125)
- **Original**: रखे। (यथा विक्रमादित्य-स्वामी अथवा तथा आकाशादि पाँच भूतोंका न्यास करे
- **Translation**: 

---

### Verse 6 (Agni Puran 0.2126)
- **Original**: रामादित्यपाद इत्यादि) सूर्यके मन्त्र पहले बताये पूर्ववत्‌ शुद्धि आदि करके पिण्डीका शोधन
- **Translation**: 

---

### Verse 7 (Agni Puran 0.2127)
- **Original**: गये हैं, उन्हींका स्थापनकालमें भी साक्षात्कार करें। फिर सदेशपद-पर्यन्त तत्त्व-पञ्ञकका न्यास
- **Translation**: 

---

### Verse 8 (Agni Puran 0.2128)
- **Original**: (प्रयोग) करना चाहिये
- **Translation**: 

---

### Verse 9 (Agni Puran 0.2129)
- **Original**: इस ग्रकार आदि आरनेय महापुराणमें “सूर्य-प्रतिष्ठा-किधिका वर्णन” जरामक निन्‍्यातबेवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 10 (Agni Puran 0.2130)
- **Original**: 99 # ++>म्य0220-..... सौवाँ अध्याय द्वारप्रतिष्ठा-विधि भगवान्‌ शंकर कहते हैं--स्कन्द! अब मैं
- **Translation**: 

---

### Verse 11 (Agni Puran 0.2131)
- **Original**: अग्रभागोंमें आत्मतत्त्व, विद्यातत्व और शिवतत्त्वका द्वारगत प्रतिष्ठाकी विधिका वर्णन करूँगा। द्वारके
- **Translation**: 

---

### Verse 12 (Agni Puran 0.2132)
- **Original**: न्‍्यास करके संनिरोधिनी-मुद्राद्वाण उनका निरोध अद्भभूत उपकरणोंका कसैले जल आदिसे संस्कार
- **Translation**: 

---

### Verse 13 (Agni Puran 0.2133)
- **Original**: करे। फिर तदनुरूप होम और जप करके, द्वारके करके उन्हें शय्यापर रखे। द्वारके मूल, मध्य और
- **Translation**: 

---

### Verse 14 (Agni Puran 0.2134)
- **Original**: अधोभागमें अनन्त देवताके मन्त्रसे बास्तु-देवताकी # सोमशम्भुकी 'कर्मकाण्ड-क्रमावली 'में इन मत्त्रोंके स्वरूप और बीज कुछ भिन्न रूपमें मिलते हैं। अत: उन्हें अधिकल रूपमें यहाँ उद्धृत किया जाता हैं -- 3» आं आधारशक्तये नम:
- **Translation**: 

---

### Verse 15 (Agni Puran 0.2135)
- **Original**: 3 ईं कन्दगाय नम: । 35% 3# नालाय नम: । 3# ऋं धर्माय नम: । 3 ऋं ज्ञानाय नमः । 3> लू बैराग्याय नमः । 3+ लूं ऐश्वर्यांय नम:
- **Translation**: 

---

### Verse 16 (Agni Puran 0.2136)
- **Original**: 3* ऊं अधर्माय नम:। <+ ऊं अज्ञानाय नम्:। 5 लूं अबैराग्याय नमः । 3> लूँ अनैश्वर्याय नम:। 3> अ: ऊर्ध्यच्छदनाय नम:। 3 हां फप्माय नम: । 3% हैं केस्तोभ्यों नमः । 3& हे कर्िकाय नम: । 3& हं पुष्करेभ्यों कम: । 35 हैं प्राम्ध्यै नमः। 35 हाँ ज्ञानवत्ये तम:। 35 हूँ क्रियायै त्म: । 3» हल वामायै तम:। 35 हलू यागौश्वर्य नम: । 35 हाँ प्लालिन्य नम: । <» हो ज्येशायै नम: । 40 हाँ रौद्पै गम: इति सर्वशक्तय: । 30 गां गौर्यासवाय तम: । 30 गो गौरीमूर्तपे गम; । <» हीं सः महागौरि रुद्रदथिते स्वाहा।--डति मूलमन्त्र:
- **Translation**: 

---

### Verse 17 (Agni Puran 0.2137)
- **Original**: गां इृदयाय मम: । गीं शिरसे स्वाहा। गूं शिखापै वषद्‌। मैं कवचाय हुम्‌। मी जेत्रेभ्यों वौदर्‌। ग: अस्थराय फटू। 3> सौ ज्ञानशक्तये जम:
- **Translation**: 

---

### Verse 18 (Agni Puran 0.2138)
- **Original**: ** सूँ क्रियाशक्तये नम:
- **Translation**: 

---

### Verse 19 (Agni Puran 0.2139)
- **Original**: लोकपालमन्त्रास्तु पूर्वोच्ता:। ऐँ सहेँ सुभगापै नम:
- **Translation**: 

---

### Verse 20 (Agni Puran 0.2140)
- **Original**: 3+ रहें ललितायै नम:। 3+ स्हं कामिन्दै नम: । 3 सही काममालिन्ये नम:। इत्येता गौरीसमानसख्य: ।
- **Translation**: 

---

