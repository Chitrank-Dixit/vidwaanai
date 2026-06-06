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

### Verse 1 (Bramha 0.1641)
- **Original**: नमस्कार है।* भी दण्ड ) हैं। आपको नमस्कार है। आप
- **Translation**: 

---

### Verse 2 (Bramha 0.1642)
- **Original**: आप ही होम और मन्त्र हैं। आपकी ध्वजा- अर्धचण्डिकेश (अर्द्धनारीश्वर), शुष्क, विकृत,
- **Translation**: 

---

### Verse 3 (Bramha 0.1643)
- **Original**: पताका श्वेत रंगकी है, आपको नमस्कार है। आप विलोहित, धूम्र और नीलग्रीव हैं। आपको नमस्कार
- **Translation**: 

---

### Verse 4 (Bramha 0.1644)
- **Original**: ही अनम्य और आप हो नमन करनेके योग्य हैं। है। आप अप्रतिरूप हैं--आपके समान दूसरा कोई
- **Translation**: 

---

### Verse 5 (Bramha 0.1645)
- **Original**: आप हर्षमग्न होकर किलकारियाँ भरनेवाले हैं। .. « सहझ्लाक्ष विरूपाक्ष त््यक्ष यक्षाधिपप्रिय। सर्वतःपाणिपादस्त्व.. सर्वतोउक्षिशिरोमुख:
- **Translation**: 

---

### Verse 6 (Bramha 0.1646)
- **Original**: सर्बतः श्रुतिमाँ्रोके सर्वमाषृत्य तिपष्ठसि । महाकर्ण: कुम्भकर्णों5र्णवालय:
- **Translation**: 

---

### Verse 7 (Bramha 0.1647)
- **Original**: गजेन्द्रकोणों गोकर्ण: शतकर्णों नमो5स्तु ते। 8 शत्ाषर्त: शतजिह्: सनातन:
- **Translation**: 

---

### Verse 8 (Bramha 0.1648)
- **Original**: त्वां गायत्रिणो अर्चयस्यपर्कमर्किण:। देवदानवगोप्ता च ब्रह्मा च त्व॑ शतक्रतु:
- **Translation**: 

---

### Verse 9 (Bramha 0.1649)
- **Original**: महामूर्ति: समुद्र: सरसां निधि:। त्वथि सर्या देवता हि गावो गोर्ठ इवासते
- **Translation**: 

---

### Verse 10 (Bramha 0.1650)
- **Original**: पश्यामि सोममग्निजलेश्वरम्‌
- **Translation**: 

---

### Verse 11 (Bramha 0.1651)
- **Original**: आदित्यमथ विष्णुं च॒ ब्रह्माणं सबृहस्पतिम्‌
- **Translation**: 

---

### Verse 12 (Bramha 0.1652)
- **Original**: करणकार्ये च॒ कर्ता कारणमेव थ। असच्य सदसच्चैव तथँव॒ प्रभब्राप्ययौ
- **Translation**: 

---

### Verse 13 (Bramha 0.1653)
- **Original**: भवाय शर्वाय रुद्राय बरदाय च। पशूतां पतये चैबव नमोःस्त्वन्धकघातिने
- **Translation**: 

---

### Verse 14 (Bramha 0.1654)
- **Original**: भ्रिशीर्षाष. त्रिशूलवरधारिणे। ज्यम्बकाय बत़्िनेश्नाय त्रिपुरक्नाय ये नम:
- **Translation**: 

---

### Verse 15 (Bramha 0.1655)
- **Original**: नमक्षण्डाय सुण्डाय विश्वयण्डधतय च। दण्डिने शद्भुकरणांय दण्डिदण्डाय यै नम:
- **Translation**: 

---

### Verse 16 (Bramha 0.1656)
- **Original**: नमो3र्थचण्डिकेशाय शुष्काय विकृताय च। विलोहिताय धूप्राय नौलग्रीवाय ये नम:
- **Translation**: 

---

### Verse 17 (Bramha 0.1657)
- **Original**: नमोस्त्वप्रतिकृपाय विरूपाय शिवाय च । सूर्याय सूर्यपतये. सूर्यध्यजपताकिने
- **Translation**: 

---

### Verse 18 (Bramha 0.1658)
- **Original**: नमः प्रमथनाशाव यृषस्कन्धाय ये नमः:। नमो हिरण्यगर्भाय हिरण्यकवचाय च
- **Translation**: 

---

### Verse 19 (Bramha 0.1659)
- **Original**: हिरण्यकृतथूडाय.. हिरण्यपतये. नमः । शत्रुधाताथ चण्डाय पर्णसह्यशयाय च
- **Translation**: 

---

### Verse 20 (Bramha 0.1660)
- **Original**: नम; स्तुताय स्तुतये स्तृथमातराय यै नमः। सर्वाय सर्वभक्षाय सर्वधूतान्तरात्पने
- **Translation**: 

---

