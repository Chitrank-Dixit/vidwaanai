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

### Verse 1 (Vaivtpuran 56.5392)
- **Original**: है--शिव+आ। 'शिव' शब्द शिव एवं कल्याण- अं ज-+7+++++++_8333€नस्‍्॒ईरप 7». »:।.,,»ैैै:ःय0थपपड्््चपहप॑पचचपचपचपोँ”7फ *शिरिति मड़लाथ॑ च वकारों दातृवाचक: । मड्जलानां प्रदाता यः स शिव: परिकीर्तित:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 56.5393)
- **Original**: नराणां संततं विश्वे शं कल्याण करोति य: । कल्थाणं मोक्षवचन स एवं शंकर: स्मृतः
- **Translation**: 

---

### Verse 3 (Vaivtpuran 56.5394)
- **Original**: ख्रह्मादीनां सुराणां च मुनौनां वेदवादिनाम्‌ । तेषां च महतां देवों महादेव: प्रकीर्तित:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 56.5395)
- **Original**: महती पूजिता विश्वे मूलप्रकृतिरीश्चरी । तस्या देव: पूजितश्च महादेषघ: स च स्मृतः
- **Translation**: 

---

### Verse 5 (Vaivtpuran 56.5396)
- **Original**: विश्वस्थानां च सर्वेषां महतामीश्वर: स्वयम्‌ । महेश्व च. तेनेम॑ प्रवदन्ति मनीषिण:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 56.5397)
- **Original**: (प्रकृतिखण्ड 56। 63--67)
- **Translation**: 

---

### Verse 7 (Vaivtpuran 56.5398)
- **Original**: अर्थमें प्रयुक्त होता है तथा 'आ' शब्द प्रिय और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 56.5399)
- **Original**: वे शक्ति हैं, इसलिये वे 'गौरी' कही गयी हैं। दाता-अर्थमें। वह देवी कल्याणस्वरूपा है, शिवदायिनी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 56.5400)
- **Original**: भगवान्‌ शिव सबके गुरु हैं और देवी उनकी है और शिवप्रिया है, इसलिये 'शिवा' कही गयी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 56.5401)
- **Original**: सती-साध्वी प्रिया शक्ति हैं। इसलिये ' गौरी' कही है। देवी दुर्गा सद्बुद्धिकी अधिष्ठात्री देवी हैं, प्रत्येक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 56.5402)
- **Original**: गयी हैं। श्रीकृष्ण ही सबके गुरु हैं और देवी युगमें विद्यमान हैं तथा पतिब्रता एवं सुशीला हैं।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 56.5403)
- **Original**: उनकी माया हैं। इसलिये भी उनको 'गौरी' कहा इसीलिये उन्हें 'सती' कहते हैं। जैसे भगवान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 56.5404)
- **Original**: गया है। 'पर्व' शब्द तिथिभेद (पूर्णिमा), पर्वभेद, नित्य हैं, उसी तरह भगवती भी “नित्या' हैं।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 56.5405)
- **Original**: कल्पभेद तथा अन्यान्य भेद अर्थमें प्रयुक्त होता प्राकृत प्रलयके समय वे अपनी मायासे परमात्मा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 56.5406)
- **Original**: है तथा “ती' शब्द ख्यातिके अर्थमें आता है। उन श्रीकृष्णमें तिरोहित रहती हैं। ब्रह्मासे लेकर तृण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 56.5407)
- **Original**: पर्व आदिमें विख्यात होनेसे उन देवीकी “पार्वती ' अथवा कीटपर्यन्त सम्पूर्ण जगत्‌ कृत्रिम होनेके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 56.5408)
- **Original**: संज्ञा है। 'पर्वन्‌' शब्द महोत्सब-विशेषके अर्थमें कारण मिथ्या ही है, परंतु दुर्गा सत्यस्वरूपा हैं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 56.5409)
- **Original**: आता है। उसकी अधिप्ठात्री देवी होनेके नाते उन्हें जैसे भगवान्‌ सत्य हैं, उसी तरह प्रकृतिदेवी भी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 56.5410)
- **Original**: “पार्बती' कहा गया है। वे देवी पर्वत (गिरिराज *सत्या' हैं। सिद्ध, ऐश्वर्य आदिके अर्थमें 'भग'
- **Translation**: 

---

### Verse 20 (Vaivtpuran 56.5411)
- **Original**: हिमालय)-की पुत्री हैं। पर्वतपर प्रकट हुई हैं शब्दका प्रयोग होता है, ऐसा समझना चाहिये।
- **Translation**: 

---

