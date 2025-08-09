import SwiftUI

struct Requirement: Identifiable, Decodable {
    let id: UUID
    let title: String
    let details: String?
}

final class RequirementsViewModel: ObservableObject {
    @Published var requirements: [Requirement] = []

    init() {
        loadRequirements()
    }

    private func loadRequirements() {
        if let url = urlForResource(named: "requirements") ?? urlForResource(named: "requirements.sample") {
            do {
                let data = try Data(contentsOf: url)
                let decoder = JSONDecoder()
                let decoded = try decoder.decode([Requirement].self, from: data)
                DispatchQueue.main.async {
                    self.requirements = decoded
                }
            } catch {
                print("Failed to load requirements: \(error)")
            }
        }
    }

    private func urlForResource(named name: String) -> URL? {
        Bundle.main.url(forResource: name, withExtension: "json")
    }
}

struct ContentView: View {
    @StateObject private var viewModel = RequirementsViewModel()

    var body: some View {
        NavigationView {
            List(viewModel.requirements) { requirement in
                VStack(alignment: .leading, spacing: 6) {
                    Text(requirement.title)
                        .font(.headline)
                    if let details = requirement.details, !details.isEmpty {
                        Text(details)
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                            .lineLimit(3)
                    }
                }
                .padding(.vertical, 4)
            }
            .navigationTitle("Requirements")
        }
    }
}

#Preview {
    ContentView()
}