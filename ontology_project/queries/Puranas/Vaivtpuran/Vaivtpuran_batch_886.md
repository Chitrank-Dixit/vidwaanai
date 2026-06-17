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

### Verse 1 (Vaivtpuran 543.16034)
- **Original**: और अस्पष्ट कौर्तिवाला उत्तम यशस्वी तथा मूर्ख चरणोंमें पुनः-पुनः प्रणिपात करने लगे। जो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16035)
- **Original**: पण्डित हो जाता है*।. (अध्याय 91-92) *+ उद्धव उचाच-- व्न्दे राधापदाम्भोज॑ ब्रह्मादिसुरवन्दितम्‌ । यत्कीर्तिकौर्तनेनैज पुनाति भुवनत्रयम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16036)
- **Original**: नमो गोलोकवासिन्ये॑ राधिकायै नमो :
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16037)
- **Original**: शतशृद्धनिवासिन्ये चन्द्रवत्ये नमो... नम:
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16038)
- **Original**: तुलसीवनवासिन्ये॑ वृन्दारण्यैू. नमो... नमः । रासमण्डलवासिन्ये रासेश्वर्य नमो. नमः
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16039)
- **Original**: विरजातीरवासिन्ये बृन्दाये॑ च नमो... नमः । वृन्दायनविलासिन्ये कृष्णाये च नमो. नम:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16040)
- **Original**: नमः कृष्णप्रियायाच शान्तायै च नमों नमः । कृण्णवक्ष:स्थिताये चतत्तप्रियायेय नमो. नमः
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16041)
- **Original**: नमो चैकुण्ठवासिन्ये महालक्ष्म्ये॑नमो.. नमः । विद्याधिष्ठात्देव्ये च सरस्वत्ये॑ नमो... नमः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16042)
- **Original**: सर्वैश्वर्याधिदेव्य॑य च. कमलायै नमो. नमः । पद्मानाभ्रप्रियायाी॑ च पद्मयाये॑च नमो नमः
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16043)
- **Original**: महाविष्णोश्ष मात्रे च पराद्याये नमो नमः
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16044)
- **Original**: नमः सिन्धुसुताय॑ च॒मर्त्यलक्ष्य्ये नमो नमः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16045)
- **Original**: नारायणप्रियाय॑ च_ नारायण्ये॑ नपो.._ नमः । नमोउस्तु किष्णुमायायै सैष्णव्ये च नमो नपः
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16046)
- **Original**: महापायास्वरूपायै सम्पदाये नमो नमः
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16047)
- **Original**: नमः कल्याणकूपिण्ये शुभाय॑ चर नमो नमः
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16048)
- **Original**: मात्रे चतुणां वेदानां साविह्यँ च नमो नमः
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16049)
- **Original**: नमो दुर्गविनाशिनये दु्गदिेब्ये नमो नपमः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16050)
- **Original**: ततेज:सु. सर्ददेवानां पुर कृतयुगे. मुदा । अधिष्ठानकृतायै च प्रकृत्य॑च नमो नमः
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16051)
- **Original**: नमस्थत्रिपुरहारिण्यै त्रिपुप॒षैे॑. नमो नमः
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16052)
- **Original**: सुन्दीषु च रम्यायै निर्णणाये नमो नमः
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16053)
- **Original**: नमो. निद्रास्यरूपायैँ निर्णुणाय॑ नमो जमः । नमो दक्षसुताये च नमः सत्य नमो तमः
- **Translation**: 

---

